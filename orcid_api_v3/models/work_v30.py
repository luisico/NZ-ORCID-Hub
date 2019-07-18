# coding: utf-8

"""
    ORCID Member

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: Latest

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from orcid_api_v3.models.citation import Citation  # noqa: F401,E501
from orcid_api_v3.models.country_v30 import CountryV30  # noqa: F401,E501
from orcid_api_v3.models.created_date_v30 import CreatedDateV30  # noqa: F401,E501
from orcid_api_v3.models.external_i_ds_v30 import ExternalIDsV30  # noqa: F401,E501
from orcid_api_v3.models.last_modified_date_v30 import LastModifiedDateV30  # noqa: F401,E501
from orcid_api_v3.models.publication_date_v30 import PublicationDateV30  # noqa: F401,E501
from orcid_api_v3.models.source_v30 import SourceV30  # noqa: F401,E501
from orcid_api_v3.models.title_v30 import TitleV30  # noqa: F401,E501
from orcid_api_v3.models.url_v30 import UrlV30  # noqa: F401,E501
from orcid_api_v3.models.work_contributors_v30 import WorkContributorsV30  # noqa: F401,E501
from orcid_api_v3.models.work_title_v30 import WorkTitleV30  # noqa: F401,E501


class WorkV30(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_date': 'CreatedDateV30',
        'last_modified_date': 'LastModifiedDateV30',
        'source': 'SourceV30',
        'put_code': 'int',
        'path': 'str',
        'title': 'WorkTitleV30',
        'journal_title': 'TitleV30',
        'short_description': 'str',
        'citation': 'Citation',
        'type': 'str',
        'publication_date': 'PublicationDateV30',
        'external_ids': 'ExternalIDsV30',
        'url': 'UrlV30',
        'contributors': 'WorkContributorsV30',
        'language_code': 'str',
        'country': 'CountryV30',
        'visibility': 'str'
    }

    attribute_map = {
        'created_date': 'created-date',
        'last_modified_date': 'last-modified-date',
        'source': 'source',
        'put_code': 'put-code',
        'path': 'path',
        'title': 'title',
        'journal_title': 'journal-title',
        'short_description': 'short-description',
        'citation': 'citation',
        'type': 'type',
        'publication_date': 'publication-date',
        'external_ids': 'external-ids',
        'url': 'url',
        'contributors': 'contributors',
        'language_code': 'language-code',
        'country': 'country',
        'visibility': 'visibility'
    }

    def __init__(self, created_date=None, last_modified_date=None, source=None, put_code=None, path=None, title=None, journal_title=None, short_description=None, citation=None, type=None, publication_date=None, external_ids=None, url=None, contributors=None, language_code=None, country=None, visibility=None):  # noqa: E501
        """WorkV30 - a model defined in Swagger"""  # noqa: E501
        self._created_date = None
        self._last_modified_date = None
        self._source = None
        self._put_code = None
        self._path = None
        self._title = None
        self._journal_title = None
        self._short_description = None
        self._citation = None
        self._type = None
        self._publication_date = None
        self._external_ids = None
        self._url = None
        self._contributors = None
        self._language_code = None
        self._country = None
        self._visibility = None
        self.discriminator = None
        if created_date is not None:
            self.created_date = created_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if source is not None:
            self.source = source
        if put_code is not None:
            self.put_code = put_code
        if path is not None:
            self.path = path
        if title is not None:
            self.title = title
        if journal_title is not None:
            self.journal_title = journal_title
        if short_description is not None:
            self.short_description = short_description
        if citation is not None:
            self.citation = citation
        if type is not None:
            self.type = type
        if publication_date is not None:
            self.publication_date = publication_date
        if external_ids is not None:
            self.external_ids = external_ids
        if url is not None:
            self.url = url
        if contributors is not None:
            self.contributors = contributors
        if language_code is not None:
            self.language_code = language_code
        if country is not None:
            self.country = country
        if visibility is not None:
            self.visibility = visibility

    @property
    def created_date(self):
        """Gets the created_date of this WorkV30.  # noqa: E501


        :return: The created_date of this WorkV30.  # noqa: E501
        :rtype: CreatedDateV30
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this WorkV30.


        :param created_date: The created_date of this WorkV30.  # noqa: E501
        :type: CreatedDateV30
        """

        self._created_date = created_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this WorkV30.  # noqa: E501


        :return: The last_modified_date of this WorkV30.  # noqa: E501
        :rtype: LastModifiedDateV30
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this WorkV30.


        :param last_modified_date: The last_modified_date of this WorkV30.  # noqa: E501
        :type: LastModifiedDateV30
        """

        self._last_modified_date = last_modified_date

    @property
    def source(self):
        """Gets the source of this WorkV30.  # noqa: E501


        :return: The source of this WorkV30.  # noqa: E501
        :rtype: SourceV30
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this WorkV30.


        :param source: The source of this WorkV30.  # noqa: E501
        :type: SourceV30
        """

        self._source = source

    @property
    def put_code(self):
        """Gets the put_code of this WorkV30.  # noqa: E501


        :return: The put_code of this WorkV30.  # noqa: E501
        :rtype: int
        """
        return self._put_code

    @put_code.setter
    def put_code(self, put_code):
        """Sets the put_code of this WorkV30.


        :param put_code: The put_code of this WorkV30.  # noqa: E501
        :type: int
        """

        self._put_code = put_code

    @property
    def path(self):
        """Gets the path of this WorkV30.  # noqa: E501


        :return: The path of this WorkV30.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this WorkV30.


        :param path: The path of this WorkV30.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def title(self):
        """Gets the title of this WorkV30.  # noqa: E501


        :return: The title of this WorkV30.  # noqa: E501
        :rtype: WorkTitleV30
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WorkV30.


        :param title: The title of this WorkV30.  # noqa: E501
        :type: WorkTitleV30
        """

        self._title = title

    @property
    def journal_title(self):
        """Gets the journal_title of this WorkV30.  # noqa: E501


        :return: The journal_title of this WorkV30.  # noqa: E501
        :rtype: TitleV30
        """
        return self._journal_title

    @journal_title.setter
    def journal_title(self, journal_title):
        """Sets the journal_title of this WorkV30.


        :param journal_title: The journal_title of this WorkV30.  # noqa: E501
        :type: TitleV30
        """

        self._journal_title = journal_title

    @property
    def short_description(self):
        """Gets the short_description of this WorkV30.  # noqa: E501


        :return: The short_description of this WorkV30.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this WorkV30.


        :param short_description: The short_description of this WorkV30.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def citation(self):
        """Gets the citation of this WorkV30.  # noqa: E501


        :return: The citation of this WorkV30.  # noqa: E501
        :rtype: Citation
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this WorkV30.


        :param citation: The citation of this WorkV30.  # noqa: E501
        :type: Citation
        """

        self._citation = citation

    @property
    def type(self):
        """Gets the type of this WorkV30.  # noqa: E501


        :return: The type of this WorkV30.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkV30.


        :param type: The type of this WorkV30.  # noqa: E501
        :type: str
        """
        allowed_values = [c.replace('_', '-').lower() for c in ["ARTISTIC_PERFORMANCE", "BOOK_CHAPTER", "BOOK_REVIEW", "BOOK", "CONFERENCE_ABSTRACT", "CONFERENCE_PAPER", "CONFERENCE_POSTER", "DATA_SET", "DICTIONARY_ENTRY", "DISCLOSURE", "DISSERTATION_THESIS", "EDITED_BOOK", "ENCYCLOPEDIA_ENTRY", "INVENTION", "JOURNAL_ARTICLE", "JOURNAL_ISSUE", "LECTURE_SPEECH", "LICENSE", "MAGAZINE_ARTICLE", "MANUAL", "NEWSLETTER_ARTICLE", "NEWSPAPER_ARTICLE", "ONLINE_RESOURCE", "OTHER", "PATENT", "PREPRINT", "REGISTERED_COPYRIGHT", "REPORT", "RESEARCH_TECHNIQUE", "RESEARCH_TOOL", "SOFTWARE", "SPIN_OFF_COMPANY", "STANDARDS_AND_POLICY", "SUPERVISED_STUDENT_PUBLICATION", "TECHNICAL_STANDARD", "TEST", "TRADEMARK", "TRANSLATION", "WEBSITE", "WORKING_PAPER", "UNDEFINED"]]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def publication_date(self):
        """Gets the publication_date of this WorkV30.  # noqa: E501


        :return: The publication_date of this WorkV30.  # noqa: E501
        :rtype: PublicationDateV30
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this WorkV30.


        :param publication_date: The publication_date of this WorkV30.  # noqa: E501
        :type: PublicationDateV30
        """

        self._publication_date = publication_date

    @property
    def external_ids(self):
        """Gets the external_ids of this WorkV30.  # noqa: E501


        :return: The external_ids of this WorkV30.  # noqa: E501
        :rtype: ExternalIDsV30
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this WorkV30.


        :param external_ids: The external_ids of this WorkV30.  # noqa: E501
        :type: ExternalIDsV30
        """

        self._external_ids = external_ids

    @property
    def url(self):
        """Gets the url of this WorkV30.  # noqa: E501


        :return: The url of this WorkV30.  # noqa: E501
        :rtype: UrlV30
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WorkV30.


        :param url: The url of this WorkV30.  # noqa: E501
        :type: UrlV30
        """

        self._url = url

    @property
    def contributors(self):
        """Gets the contributors of this WorkV30.  # noqa: E501


        :return: The contributors of this WorkV30.  # noqa: E501
        :rtype: WorkContributorsV30
        """
        return self._contributors

    @contributors.setter
    def contributors(self, contributors):
        """Sets the contributors of this WorkV30.


        :param contributors: The contributors of this WorkV30.  # noqa: E501
        :type: WorkContributorsV30
        """

        self._contributors = contributors

    @property
    def language_code(self):
        """Gets the language_code of this WorkV30.  # noqa: E501


        :return: The language_code of this WorkV30.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this WorkV30.


        :param language_code: The language_code of this WorkV30.  # noqa: E501
        :type: str
        """
        allowed_values = ["ab", "aa", "af", "ak", "sq", "am", "ar", "an", "hy", "as", "av", "ae", "ay", "az", "bm", "ba", "eu", "be", "bn", "bh", "bi", "bs", "br", "bg", "my", "ca", "ch", "ce", "zh_CN", "zh_TW", "cu", "cv", "kw", "co", "cr", "hr", "cs", "da", "dv", "nl", "dz", "en", "eo", "et", "ee", "fo", "fj", "fi", "fr", "fy", "ff", "gl", "lg", "ka", "de", "el", "kl", "gn", "gu", "ht", "ha", "iw", "hz", "hi", "ho", "hu", "is", "io", "ig", "in", "ia", "ie", "iu", "ik", "ga", "it", "ja", "jv", "kn", "kr", "ks", "kk", "km", "ki", "rw", "ky", "kv", "kg", "ko", "ku", "kj", "lo", "la", "lv", "li", "ln", "lt", "lu", "lb", "mk", "mg", "ms", "ml", "mt", "gv", "mi", "mr", "mh", "mo", "mn", "na", "nv", "ng", "ne", "nd", "se", "no", "nb", "nn", "ny", "oc", "oj", "or", "om", "os", "pi", "pa", "fa", "pl", "pt", "ps", "qu", "rm", "ro", "rn", "ru", "sm", "sg", "sa", "sc", "gd", "sr", "sn", "ii", "sd", "si", "sk", "sl", "so", "nr", "st", "es", "su", "sw", "ss", "sv", "tl", "ty", "tg", "ta", "tt", "te", "th", "bo", "ti", "to", "ts", "tn", "tr", "tk", "tw", "ug", "uk", "ur", "uz", "ve", "vi", "vo", "wa", "cy", "wo", "xh", "ji", "yo", "za", "zu"]  # noqa: E501
        if language_code not in allowed_values:
            raise ValueError(
                "Invalid value for `language_code` ({0}), must be one of {1}"  # noqa: E501
                .format(language_code, allowed_values)
            )

        self._language_code = language_code

    @property
    def country(self):
        """Gets the country of this WorkV30.  # noqa: E501


        :return: The country of this WorkV30.  # noqa: E501
        :rtype: CountryV30
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this WorkV30.


        :param country: The country of this WorkV30.  # noqa: E501
        :type: CountryV30
        """

        self._country = country

    @property
    def visibility(self):
        """Gets the visibility of this WorkV30.  # noqa: E501


        :return: The visibility of this WorkV30.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this WorkV30.


        :param visibility: The visibility of this WorkV30.  # noqa: E501
        :type: str
        """
        allowed_values = ["LIMITED", "REGISTERED_ONLY", "PUBLIC", "PRIVATE", "public", "private",
                          "limited", "registered-only"]  # noqa: E501
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WorkV30, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkV30):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
