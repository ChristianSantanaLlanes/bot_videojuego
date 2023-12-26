from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class DatumAttributes:
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DatumAttributes':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        published_at = from_union([from_datetime, from_none], obj.get("publishedAt"))
        return DatumAttributes(name, created_at, updated_at, published_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        if self.published_at is not None:
            result["publishedAt"] = from_union([lambda x: x.isoformat(), from_none], self.published_at)
        return result


@dataclass
class Datum:
    id: Optional[int] = None
    attributes: Optional[DatumAttributes] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        attributes = from_union([DatumAttributes.from_dict, from_none], obj.get("attributes"))
        return Datum(id, attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.attributes is not None:
            result["attributes"] = from_union([lambda x: to_class(DatumAttributes, x), from_none], self.attributes)
        return result


@dataclass
class Caracterisiticas:
    data: Optional[List[Datum]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Caracterisiticas':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        return Caracterisiticas(data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.data is not None:
            result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        return result


@dataclass
class ProviderMetadata:
    public_id: Optional[str] = None
    resource_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProviderMetadata':
        assert isinstance(obj, dict)
        public_id = from_union([from_str, from_none], obj.get("public_id"))
        resource_type = from_union([from_str, from_none], obj.get("resource_type"))
        return ProviderMetadata(public_id, resource_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.public_id is not None:
            result["public_id"] = from_union([from_str, from_none], self.public_id)
        if self.resource_type is not None:
            result["resource_type"] = from_union([from_str, from_none], self.resource_type)
        return result


@dataclass
class Thumbnail:
    path: None
    ext: Optional[str] = None
    url: Optional[str] = None
    hash: Optional[str] = None
    mime: Optional[str] = None
    name: Optional[str] = None
    size: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    provider_metadata: Optional[ProviderMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Thumbnail':
        assert isinstance(obj, dict)
        path = from_none(obj.get("path"))
        ext = from_union([from_str, from_none], obj.get("ext"))
        url = from_union([from_str, from_none], obj.get("url"))
        hash = from_union([from_str, from_none], obj.get("hash"))
        mime = from_union([from_str, from_none], obj.get("mime"))
        name = from_union([from_str, from_none], obj.get("name"))
        size = from_union([from_float, from_none], obj.get("size"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        provider_metadata = from_union([ProviderMetadata.from_dict, from_none], obj.get("provider_metadata"))
        return Thumbnail(path, ext, url, hash, mime, name, size, width, height, provider_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.path is not None:
            result["path"] = from_none(self.path)
        if self.ext is not None:
            result["ext"] = from_union([from_str, from_none], self.ext)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.hash is not None:
            result["hash"] = from_union([from_str, from_none], self.hash)
        if self.mime is not None:
            result["mime"] = from_union([from_str, from_none], self.mime)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.size is not None:
            result["size"] = from_union([to_float, from_none], self.size)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.provider_metadata is not None:
            result["provider_metadata"] = from_union([lambda x: to_class(ProviderMetadata, x), from_none], self.provider_metadata)
        return result


@dataclass
class Formats:
    thumbnail: Optional[Thumbnail] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Formats':
        assert isinstance(obj, dict)
        thumbnail = from_union([Thumbnail.from_dict, from_none], obj.get("thumbnail"))
        return Formats(thumbnail)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.thumbnail is not None:
            result["thumbnail"] = from_union([lambda x: to_class(Thumbnail, x), from_none], self.thumbnail)
        return result


@dataclass
class DataAttributes:
    alternative_text: None
    caption: None
    preview_url: None
    name: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    formats: Optional[Formats] = None
    hash: Optional[str] = None
    ext: Optional[str] = None
    mime: Optional[str] = None
    size: Optional[float] = None
    url: Optional[str] = None
    provider: Optional[str] = None
    provider_metadata: Optional[ProviderMetadata] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataAttributes':
        assert isinstance(obj, dict)
        alternative_text = from_none(obj.get("alternativeText"))
        caption = from_none(obj.get("caption"))
        preview_url = from_none(obj.get("previewUrl"))
        name = from_union([from_str, from_none], obj.get("name"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        formats = from_union([Formats.from_dict, from_none], obj.get("formats"))
        hash = from_union([from_str, from_none], obj.get("hash"))
        ext = from_union([from_str, from_none], obj.get("ext"))
        mime = from_union([from_str, from_none], obj.get("mime"))
        size = from_union([from_float, from_none], obj.get("size"))
        url = from_union([from_str, from_none], obj.get("url"))
        provider = from_union([from_str, from_none], obj.get("provider"))
        provider_metadata = from_union([ProviderMetadata.from_dict, from_none], obj.get("provider_metadata"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        return DataAttributes(alternative_text, caption, preview_url, name, width, height, formats, hash, ext, mime, size, url, provider, provider_metadata, created_at, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.alternative_text is not None:
            result["alternativeText"] = from_none(self.alternative_text)
        if self.caption is not None:
            result["caption"] = from_none(self.caption)
        if self.preview_url is not None:
            result["previewUrl"] = from_none(self.preview_url)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.formats is not None:
            result["formats"] = from_union([lambda x: to_class(Formats, x), from_none], self.formats)
        if self.hash is not None:
            result["hash"] = from_union([from_str, from_none], self.hash)
        if self.ext is not None:
            result["ext"] = from_union([from_str, from_none], self.ext)
        if self.mime is not None:
            result["mime"] = from_union([from_str, from_none], self.mime)
        if self.size is not None:
            result["size"] = from_union([to_float, from_none], self.size)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.provider is not None:
            result["provider"] = from_union([from_str, from_none], self.provider)
        if self.provider_metadata is not None:
            result["provider_metadata"] = from_union([lambda x: to_class(ProviderMetadata, x), from_none], self.provider_metadata)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result


@dataclass
class Data:
    id: Optional[int] = None
    attributes: Optional[DataAttributes] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        attributes = from_union([DataAttributes.from_dict, from_none], obj.get("attributes"))
        return Data(id, attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.attributes is not None:
            result["attributes"] = from_union([lambda x: to_class(DataAttributes, x), from_none], self.attributes)
        return result


@dataclass
class Cover:
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Cover':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return Cover(data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


@dataclass
class GameAttributes:
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None
    description: Optional[str] = None
    req_min: Optional[str] = None
    rec_rec: Optional[str] = None
    trailer_url: Optional[str] = None
    generos: Optional[Caracterisiticas] = None
    caracterisiticas: Optional[Caracterisiticas] = None
    vistas: Optional[Caracterisiticas] = None
    companias: Optional[Caracterisiticas] = None
    cover: Optional[Cover] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GameAttributes':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        published_at = from_union([from_datetime, from_none], obj.get("publishedAt"))
        description = from_union([from_str, from_none], obj.get("description"))
        req_min = from_union([from_str, from_none], obj.get("req_min"))
        rec_rec = from_union([from_str, from_none], obj.get("rec_rec"))
        trailer_url = from_union([from_str, from_none], obj.get("trailer_url"))
        generos = from_union([Caracterisiticas.from_dict, from_none], obj.get("generos"))
        caracterisiticas = from_union([Caracterisiticas.from_dict, from_none], obj.get("caracterisiticas"))
        vistas = from_union([Caracterisiticas.from_dict, from_none], obj.get("vistas"))
        companias = from_union([Caracterisiticas.from_dict, from_none], obj.get("companias"))
        cover = from_union([Cover.from_dict, from_none], obj.get("cover"))
        return GameAttributes(name, created_at, updated_at, published_at, description, req_min, rec_rec, trailer_url, generos, caracterisiticas, vistas, companias, cover)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        if self.published_at is not None:
            result["publishedAt"] = from_union([lambda x: x.isoformat(), from_none], self.published_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.req_min is not None:
            result["req_min"] = from_union([from_str, from_none], self.req_min)
        if self.rec_rec is not None:
            result["rec_rec"] = from_union([from_str, from_none], self.rec_rec)
        if self.trailer_url is not None:
            result["trailer_url"] = from_union([from_str, from_none], self.trailer_url)
        if self.generos is not None:
            result["generos"] = from_union([lambda x: to_class(Caracterisiticas, x), from_none], self.generos)
        if self.caracterisiticas is not None:
            result["caracterisiticas"] = from_union([lambda x: to_class(Caracterisiticas, x), from_none], self.caracterisiticas)
        if self.vistas is not None:
            result["vistas"] = from_union([lambda x: to_class(Caracterisiticas, x), from_none], self.vistas)
        if self.companias is not None:
            result["companias"] = from_union([lambda x: to_class(Caracterisiticas, x), from_none], self.companias)
        if self.cover is not None:
            result["cover"] = from_union([lambda x: to_class(Cover, x), from_none], self.cover)
        return result


@dataclass
class Game:
    id: Optional[int] = None
    attributes: Optional[GameAttributes] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Game':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        attributes = from_union([GameAttributes.from_dict, from_none], obj.get("attributes"))
        return Game(id, attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.attributes is not None:
            result["attributes"] = from_union([lambda x: to_class(GameAttributes, x), from_none], self.attributes)
        return result


def game_from_dict(s: Any) -> Game:
    return Game.from_dict(s)


def game_to_dict(x: Game) -> Any:
    return to_class(Game, x)



