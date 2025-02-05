from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Union,
)

import streamlit as st
from st_configurator.layout_schema import LayoutConfig, PageConfig
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
        config: LayoutConfig,
    ):
        component = config.component
        args = config.args
        kwargs = config.kwargs
        result_key = config.result_key
        result = self._placeholder_wrapper(component, args, kwargs, result_key)
        return result

    def __is_context_manager(self, obj) -> bool:
        return hasattr(obj, "__enter__") and hasattr(obj, "__exit__")

    def _handle_objects(self, obj: Any, children: List[LayoutConfig]) -> None:
        if isinstance(obj, (list, tuple)):
            for i, obj in enumerate(obj):
                if children[i] is not None:
                    with obj:
                        self.render_layout([children[i]])
        elif self.__is_context_manager(obj):
            with obj:
                self.render_layout(children)
        else:
            obj(self.render_layout)(children)

    def _children_parser(self, config: LayoutConfig):
        component = config.component
        args = config.args
        kwargs = config.kwargs
        children = config.children

        obj = component(*args, **kwargs)

        if not obj or not children:
            return

        self._handle_objects(obj, children)

    def _check_condition(
        self, condition: Union[PlaceholderValue, LayoutConfig, None]
    ) -> bool:
        if condition is None:
            return True

        if isinstance(condition, PlaceholderValue):
            return bool(condition.get())

        return self._build_component(condition)

    def render_layout(self, configs: Sequence[LayoutConfig | None]) -> None:
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