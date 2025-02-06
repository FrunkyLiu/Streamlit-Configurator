from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

if TYPE_CHECKING:
    from st_configurator.placeholder import PlaceholderValue


@dataclass
class ComponentConfig:
    component: Callable
    args: Tuple[Union[PlaceholderValue, Any], ...] = ()
    kwargs: Dict[str, Union[PlaceholderValue, Any]] = field(
        default_factory=dict
    )
    children: List["ComponentConfig"] = field(default_factory=list)
    condition: Optional[Union[PlaceholderValue, "ComponentConfig"]] = None
    result_key: Optional[PlaceholderValue] = None

    def update(
        self,
        args: Optional[Tuple[Union[PlaceholderValue, Any], ...]] = None,
        kwargs: Optional[Dict[str, Union[PlaceholderValue, Any]]] = None,
        children: Optional[List["ComponentConfig"]] = None,
        condition: Optional[Union[PlaceholderValue, "ComponentConfig"]] = None,
        result_key: Optional[PlaceholderValue] = None,
    ) -> "ComponentConfig":
        """
        Returns a new ComponentConfig with updated fields.

        Updates differ per argument:
        - args: If provided, replaces the current 'args' entirely.
        - kwargs: If provided, merges the new items into the current 'kwargs',
        overwriting any conflicting keys.
        - children: If provided, replaces the current 'children' entirely.
        - condition: If provided, directly replaces the current 'condition'.
        - result_key: If provided, directly replaces the current 'result_key'.

        Any fields not specified will remain unchanged.
        """
        return replace(
            self,
            args=args if args is not None else self.args,
            kwargs=(
                {**self.kwargs, **kwargs}
                if kwargs is not None
                else self.kwargs
            ),
            children=children if children is not None else self.children,
            condition=condition if condition is not None else self.condition,
            result_key=(
                result_key if result_key is not None else self.result_key
            ),
        )


@dataclass
class PageConfig:
    page_tag: str
    body: List[ComponentConfig]
    sidebar: List[ComponentConfig] = field(default_factory=list)