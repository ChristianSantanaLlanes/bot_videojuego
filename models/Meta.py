from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Pagination:
    page: Optional[int] = None
    page_size: Optional[int] = None
    page_count: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Pagination':
        assert isinstance(obj, dict)
        page = from_union([from_int, from_none], obj.get("page"))
        page_size = from_union([from_int, from_none], obj.get("pageSize"))
        page_count = from_union([from_int, from_none], obj.get("pageCount"))
        total = from_union([from_int, from_none], obj.get("total"))
        return Pagination(page, page_size, page_count, total)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.page is not None:
            result["page"] = from_union([from_int, from_none], self.page)
        if self.page_size is not None:
            result["pageSize"] = from_union([from_int, from_none], self.page_size)
        if self.page_count is not None:
            result["pageCount"] = from_union([from_int, from_none], self.page_count)
        if self.total is not None:
            result["total"] = from_union([from_int, from_none], self.total)
        return result


@dataclass
class Meta:
    pagination: Optional[Pagination] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        pagination = from_union([Pagination.from_dict, from_none], obj.get("pagination"))
        return Meta(pagination)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.pagination is not None:
            result["pagination"] = from_union([lambda x: to_class(Pagination, x), from_none], self.pagination)
        return result


def meta_from_dict(s: Any) -> Meta:
    return Meta.from_dict(s)


def meta_to_dict(x: Meta) -> Any:
    return to_class(Meta, x)
