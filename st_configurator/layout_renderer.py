from typing import (
    Any,
    Callable,
    ContextManager,
    Iterable,
    Mapping,
    Optional,
    Sequence,
    Union,
)

import streamlit as st

from st_configurator.layout_schema import ComponentConfig, PageConfig
from st_configurator.placeholder import Placeholder, PlaceholderValue


class PageRenderer:

    def _placeholder_wrapper(
        self,
        component: Callable,
        args: Iterable,
        kwargs: Mapping,
        result_key: Optional[PlaceholderValue] = None,
    ):
        args, kwargs = Placeholder.update_param_placeholders(
            component, args, kwargs, result_key
        )
        result = component(*args, **kwargs)
        if result_key:
            result_key.set(result)
        return result

    def _build_component(
        self,
        config: ComponentConfig,
    ):
        component = config.component
        args = config.args
        kwargs = config.kwargs
        result_key = config.result_key
        result = self._placeholder_wrapper(component, args, kwargs, result_key)
        return result

    def __is_context_manager(self, obj) -> bool:
        return hasattr(obj, "__enter__") and hasattr(obj, "__exit__")

    def _handle_context_manager(
        self, obj: ContextManager, children: Sequence[ComponentConfig | None]
    ) -> None:
        with obj:
            self.render_layout(children)

    def _handle_decorator(
        self, obj: Callable[..., Callable], children: Sequence[ComponentConfig]
    ) -> None:
        decorated_render = obj(self.render_layout)
        decorated_render(children)

    def _handle_single_children(
        self, obj: ContextManager, children: Sequence[ComponentConfig | None]
    ) -> None:
        self._handle_context_manager(obj, children)

    def _handle_nested_children(
        self,
        obj: Sequence[ContextManager],
        children: Sequence[Sequence[ComponentConfig | None]],
    ) -> None:
        transposed_children = list(map(list, zip(*children)))
        for i, obj_item in enumerate(obj):
            self._handle_context_manager(obj_item, transposed_children[i])

    def _handle_children(
        self,
        obj: Any,
        children: Sequence,
    ) -> None:
        if children and isinstance(
            children[0], (list, tuple)
        ):
            self._handle_nested_children(obj, children)
        else:
            if isinstance(obj, (list, tuple)):
                for i, obj_item in enumerate(obj):
                    self._handle_context_manager(obj_item, [children[i]])
            elif self.__is_context_manager(obj):
                self._handle_single_children(obj, children)
            else:
                self._handle_decorator(obj, children)

    def _children_parser(self, config: ComponentConfig):
        component = config.component
        args = config.args
        kwargs = config.kwargs
        children = config.children

        obj = component(*args, **kwargs)

        if not obj or not children:
            return

        self._handle_children(obj, children)

    def _check_condition(
        self, condition: Union[PlaceholderValue, ComponentConfig, None]
    ) -> bool:
        if condition is None:
            return True

        if isinstance(condition, PlaceholderValue):
            return bool(condition.get())

        return self._build_component(condition)

    def render_layout(self, configs: Sequence[ComponentConfig | None]) -> None:
        for config in configs:
            if config is None:
                continue

            # Check conditions early and continue if not met
            if not self._check_condition(config.condition):
                continue

            # Handle children configurations
            if config.children:
                self._children_parser(config)
                continue

            # Process regular streamlit elements
            self._build_component(config)
        return

    def render_page(self, configs: PageConfig) -> None:
        page_tag = configs.page_tag
        sidebar_configs = configs.sidebar
        body_configs = configs.body
        Placeholder._CURRENT_PAGE.set(page_tag)
        if sidebar_configs:
            with st.sidebar:
                self.render_layout(sidebar_configs)
        self.render_layout(body_configs)
        return
