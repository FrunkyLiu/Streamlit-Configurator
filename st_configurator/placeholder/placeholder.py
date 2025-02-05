import inspect

import streamlit as st


class PlaceholderValue:
    def __init__(self, default=None, invert=False, persist=False, name=None):
        """Initialize the placeholder.
        A placeholder represents a widget configuration item, offering basic settings for configuration like default, inversion and persistence.
        Args:
            default: Default value for the configuration item. Defaults to None.
            invert (bool): Whether to invert the value. Defaults to False.
            persist (bool): Whether to persist the value. Defaults to False.
            name (str, optional): Custom name for the configuration item. Will be auto-generated if not specified.
                Defaults to None.
        """
        self._name = name
        self._default = default
        self.invert = invert
        self.persist = persist

    def __call__(self, default=None, invert=False, persist=False):
        self._default = default
        self.invert = invert
        self.persist = persist
        return self

    def get_key(self):
        if self._name == "_CURRENT_PAGE":
            return self._name
        current_page = Placeholder._CURRENT_PAGE.get()
        return f"{current_page}_{self._name}"

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, obj, value):
        self.set(value)

    def __get__(self, obj, objtype=None):
        return self

    def set(self, value, *, key=None):
        if key is None:
            key = self.get_key()
        session_state = st.session_state.setdefault("_placeholder_values", {})
        session_state[key] = value

    def get(self, *, key=None):
        if key is None:
            key = self.get_key()

        if key in st.session_state:
            val = st.session_state[key]
        elif key in st.session_state.get("_placeholder_values", {}):
            val = st.session_state["_placeholder_values"].get(key, None)
        else:
            val = self._default

        if self.persist:
            persist_data = st.session_state.setdefault("_persist", {})
            key_data = persist_data.setdefault(key, {})
            if "first" not in key_data:
                key_data["first"] = val
            elif "last" not in key_data and key_data["first"] != val:
                key_data["last"] = val
            elif "last" in key_data:
                val = key_data["last"]

        if self.invert:
            val = not bool(val)
        return val

    def __repr__(self):
        return f"<PlaceholderValue name={self._name}>"


class _PlaceholderMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        for key, value in attrs.items():
            if key.startswith("__") and key.endswith("__"):
                new_attrs[key] = value
            elif hasattr(value, "__get__") or hasattr(value, "__set__"):
                new_attrs[key] = value
            else:
                new_attrs[key] = PlaceholderValue(name=key, default=value)
        return super().__new__(mcs, name, bases, new_attrs)

    def __setattr__(cls, name, value):
        if isinstance(value, PlaceholderValue):
            value.__set_name__(cls, name)
            descriptor = value
        elif hasattr(cls, name):
            descriptor = getattr(cls, name)
            descriptor.set(value)
        else:
            descriptor = PlaceholderValue(name=name, default=value)
        super(_PlaceholderMeta, cls).__setattr__(name, descriptor)


class Placeholder(metaclass=_PlaceholderMeta):
    _CURRENT_PAGE = PlaceholderValue()

    @classmethod
    def update_param_placeholders(cls, obj, obj_args, obj_kwargs, result_key):
        def _resolve(item):
            if isinstance(item, PlaceholderValue):
                return item.get()
            else:
                return item

        sig = inspect.signature(obj)
        has_key_param = "key" in sig.parameters
        new_args = [_resolve(arg) for arg in obj_args]
        new_kwargs = {k: _resolve(v) for k, v in obj_kwargs.items()}
        if has_key_param and result_key:
            new_kwargs["key"] = result_key.get_key()
        return new_args, new_kwargs

    @classmethod
    def set_attr(cls, name, value):
        setattr(cls, name, value)


__all__ = ["Placeholder", "PlaceholderValue"]