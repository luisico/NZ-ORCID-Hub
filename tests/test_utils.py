# -*- coding: utf-8 -*-
"""Tests for util functions."""
from unittest.mock import patch

from flask_login import login_user

from orcid_hub import utils
from orcid_hub.models import (AffiliationRecord, Organisation, Role, User, UserOrg, Task, FundingContributor,
    FundingRecord, UserInvitation, OrcidToken, ExternalId)
from peewee import JOIN
from itertools import groupby
from unittest.mock import patch
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def test_append_qs():
    """Test URL modication."""
    assert utils.append_qs(
        "https://abc.com/bar?p=foo", abc=123,
        p2="ABC") == "https://abc.com/bar?p=foo&abc=123&p2=ABC"
    assert utils.append_qs(
        "https://abc.com/bar", abc=123, p2="ABC") == "https://abc.com/bar?abc=123&p2=ABC"
    assert utils.append_qs(
        "https://abc.com/bar?p=foo", p2="A&B&C D") == "https://abc.com/bar?p=foo&p2=A%26B%26C+D"


def test_generate_confirmation_token():
    """Test to generate confirmation token."""
    token = utils.generate_confirmation_token(["testemail@example.com"])
    data = utils.confirm_token(token)
    # Test positive testcase
    assert 'testemail@example.com' == data[0]
    import time
    time.sleep(2)
    assert not utils.confirm_token(token, expiration=1)


def test_track_event(request_ctx):
    """Test to track event."""
    category = "test"
    action = "test"
    label = None
    value = 0

    u = User(
        email="test123@test.test.net",
        name="TEST USER",
        username="test123",
        roles=Role.RESEARCHER,
        orcid=None,
        confirmed=True)
    u.save()

    with request_ctx("/"):
        login_user(u)
        rv = utils.track_event(category, action, label, value)
        assert rv.status_code == 200


def test_set_server_name(app):
    """Test to set server name."""
    utils.set_server_name()
    server_name = app.config.get("SERVER_NAME")
    utils.set_server_name()
    assert server_name == app.config.get("SERVER_NAME")
    app.config["SERVER_NAME"] = "abc.orcidhub.org.nz"
    utils.set_server_name()
    assert "abc.orcidhub.org.nz" == app.config.get("SERVER_NAME")


def send_mail_mock(template_filename,
                   recipient,
                   cc_email=None,
                   sender=None,
                   reply_to=None,
                   subject=None,
                   base=None,
                   logo=None,
                   **kwargs):
    """Mock email invitation."""
    logger.info(f"***\nActually email invitation was mocked, so no email sent!!!!!")
    return True


@patch("orcid_hub.utils.send_email", side_effect=send_mail_mock)
def test_send_user_invitation(test_db, request_ctx):
    """Test to send user invitation."""
    org = Organisation(
        id=1,
        name="THE ORGANISATION",
        tuakiri_name="THE ORGANISATION",
        confirmed=True,
        orcid_client_id="CLIENT ID",
        orcid_secret="Client Secret",
        city="CITY",
        country="COUNTRY",
        disambiguation_org_id="ID",
        disambiguation_org_source="SOURCE")

    inviter = User(
        email="test123@mailinator.com",
        name="TEST USER",
        username="test123",
        roles=Role.RESEARCHER,
        orcid=None,
        confirmed=True,
        organisation=org)

    u = User(
        email="test123445@mailinator.com",
        name="TEST USER",
        username="test123",
        roles=Role.RESEARCHER,
        orcid=None,
        confirmed=True,
        organisation=org)
    u.save()
    user_org = UserOrg(user=u, org=org)
    user_org.save()
    task = Task(id=123, org=org)
    task.save()
    email = "test123445@mailinator.com"
    first_name = "TEST"
    last_name = "Test"
    affiliation_types = {"staff"}
    with patch("smtplib.SMTP") as mock_smtp, request_ctx("/") as ctxx:

        instance = mock_smtp.return_value
        error = {
            email:
                (450, "Requested mail action not taken: mailbox unavailable")
        }
        instance.orcid_hub.utils.send_email.return_value = error
        result = instance.orcid_hub.utils.send_email(template_filename="xyz.html", recipient=u.email)
        utils.send_user_invitation(
            inviter=inviter,
            org=org,
            email=email,
            first_name=first_name,
            last_name=last_name,
            affiliation_types=affiliation_types,
            task_id=task.id)
        rv = ctxx.app.full_dispatch_request()
        assert rv.status_code == 200
        assert instance.utils.send_user_invitation.called == True  # noqa: E712
        assert (450, 'Requested mail action not taken: mailbox unavailable') == result[email]


@patch("orcid_hub.utils.send_email", side_effect=send_mail_mock)
def test_send_funding_invitation(test_db, request_ctx):
    """Test to send user invitation."""
    org = Organisation(
        id=1,
        name="THE ORGANISATION",
        tuakiri_name="THE ORGANISATION",
        confirmed=True,
        orcid_client_id="CLIENT ID",
        orcid_secret="Client Secret",
        city="CITY",
        country="COUNTRY",
        disambiguation_org_id="ID",
        disambiguation_org_source="SOURCE")

    inviter = User(
        email="test1as237@mailinator.com",
        name="TEST USER",
        username="test123",
        roles=Role.RESEARCHER,
        orcid=None,
        confirmed=True,
        organisation=org)

    u = User(
        email="test1234456@mailinator.com",
        name="TEST USER",
        username="test123",
        roles=Role.RESEARCHER,
        orcid=None,
        confirmed=True,
        organisation=org)
    u.save()
    user_org = UserOrg(user=u, org=org)
    user_org.save()
    task = Task(org=org, task_type=1)
    task.save()
    email = "test1234456@mailinator.com"
    fr = FundingRecord(task=task.id, title="xyz", type="Award")
    fr.save()
    fc = FundingContributor(funding_record=fr.id, email=email)
    fc.save()
    with request_ctx("/") as ctxx:
        utils.send_funding_invitation(
            inviter=inviter,
            org=org,
            email=email,
            name=u.name,
            task_id=task.id)
        rv = ctxx.app.full_dispatch_request()
        assert rv.status_code == 200


def get_record_mock():
    """Mock profile api call."""
    return {'activities-summary':
                {'last-modified-date': {'value': 1513136293368},    # noqa: E127
                 'educations': {'last-modified-date': None, 'education-summary': [],
                                'path': '/0000-0002-3879-2651/educations'},
                 "employments": {
                     "last-modified-date": {
                         "value": 1511401310144
                     },
                     "employment-summary": [
                         {
                             "created-date": {
                                 "value": 1511401310144
                             },
                             "last-modified-date": {
                                 "value": 1511401310144
                             },
                             "source": {
                                 "source-orcid": None,
                                 "source-client-id": {
                                     "uri": "http://sandbox.orcid.org/client/APP-5ZVH4JRQ0C27RVH5",
                                     "path": "APP-5ZVH4JRQ0C27RVH5",
                                     "host": "sandbox.orcid.org"
                                 },
                                 "source-name": {
                                     "value": "The University of Auckland - MyORCiD"
                                 }
                             },
                             "department-name": None,
                             "role-title": None,
                             "start-date": None,
                             "end-date": None,
                             "organization": {
                                 "name": "The University of Auckland",
                                 "address": {
                                     "city": "Auckland",
                                     "region": None,
                                     "country": "NZ"
                                 },
                                 "disambiguated-organization": None
                             },
                             "visibility": "PUBLIC",
                             "put-code": 29272,
                             "path": "/0000-0003-1255-9023/employment/29272"
                         }
                     ],
                     "path": "/0000-0003-1255-9023/employments"
                 },
                 'fundings': {'last-modified-date': {'value': 1513136293368}, 'group': [
                     {'last-modified-date': {'value': 1513136293368}, 'external-ids': {
                         'external-id': [
                             {'external-id-type': 'grant_number', 'external-id-value': 'GNS1701',
                              'external-id-url': None, 'external-id-relationship': 'SELF'},
                             {'external-id-type': 'grant_number', 'external-id-value': '17-GNS-022',
                              'external-id-url': None, 'external-id-relationship': 'SELF'}]},
                      'funding-summary': [{'created-date': {'value': 1511935227017},
                                           'last-modified-date': {'value': 1513136293368},
                                           'source': {'source-orcid': None, 'source-client-id': {
                                               'uri': 'http://sandbox.orcid.org/client/APP-5ZVH4JRQ0C27RVH5',
                                               'path': 'APP-5ZVH4JRQ0C27RVH5',
                                               'host': 'sandbox.orcid.org'}, 'source-name': {
                                               'value': 'The University of Auckland - MyORCiD'}},
                                           'title': {'title': {
                                               'value': 'Probing the crust with zirco'},
                                               'translated-title': {'value': 'नमस्ते',
                                                                    'language-code': 'hi'}},
                                           'type': 'CONTRACT', 'start-date': None,
                                           'end-date': {'year': {'value': '2025'}, 'month': None,
                                                        'day': None},
                                           'organization': {'name': 'Royal Society Te Apārangi'},
                                           'put-code': 9597,
                                           'path': '/0000-0002-3879-2651/funding/9597'}]}],
                              'path': '/0000-0002-3879-2651/fundings'},
                 'path': '/0000-0002-3879-2651/activities'}, 'path': '/0000-0002-3879-2651'}


def create_or_update_fund_or_aff_mock(affiliation=None, task_by_user=None, *args, **kwargs):
    """Mock funding api call."""
    return (12399, "12344", True)


@patch("orcid_hub.orcid_client.MemberAPI.create_or_update_funding", side_effect=create_or_update_fund_or_aff_mock)
@patch("orcid_hub.orcid_client.MemberAPI.get_record", side_effect=get_record_mock)
def test_create_or_update_funding(patch, test_db, request_ctx):
    """Test create or update funding."""
    org = Organisation(
        name="THE ORGANISATION",
        tuakiri_name="THE ORGANISATION",
        confirmed=True,
        orcid_client_id="APP-5ZVH4JRQ0C27RVH5",
        orcid_secret="Client Secret",
        city="CITY",
        country="COUNTRY",
        disambiguation_org_id="ID",
        disambiguation_org_source="SOURCE")
    org.save()

    u = User(
        email="test1234456@mailinator.com",
        name="TEST USER",
        username="test123",
        roles=Role.RESEARCHER,
        orcid="123",
        confirmed=True,
        organisation=org)
    u.save()
    user_org = UserOrg(user=u, org=org)
    user_org.save()

    t = Task(
        org=org,
        filename="xyz.json",
        created_by=u,
        updated_by=u,
        task_type=1)
    t.save()

    fr = FundingRecord(
        task=t,
        title="Test titile",
        translated_title="Test title",
        translated_title_language_code="Test",
        type="Test type",
        organization_defined_type="Test org",
        short_description="Test desc",
        amount="1000",
        currency="USD",
        org_name="Test_orgname",
        city="Test city",
        region="Test",
        country="Test",
        disambiguated_org_identifier="Test_dis",
        disambiguation_source="Test_source",
        is_active=True,
        visibility="Test_visibity")
    fr.save()

    fc = FundingContributor(
        funding_record=fr,
        name="Test",
        email="test1234456@mailinator.com",
        orcid="123",
        role="Researcher")
    fc.save()

    ext_id = ExternalId(
        funding_record=fr,
        type="Test_type",
        value="Test_value",
        url="Test",
        relationship="SELF")
    ext_id.save()

    ui = UserInvitation(
        invitee=u,
        inviter=u,
        org=org,
        task=t,
        email="test1234456@mailinator.com",
        token="xyztoken")
    ui.save()

    ot = OrcidToken(
        user=u,
        org=org,
        scope="/read-limited,/activities/update",
        access_token="Test_token")
    ot.save()

    tasks = (Task.select(
        Task, FundingRecord, FundingContributor,
        User, UserInvitation.id.alias("invitation_id"), OrcidToken).where(
            FundingRecord.processed_at.is_null(), FundingContributor.processed_at.is_null(),
            FundingRecord.is_active,
            (OrcidToken.id.is_null(False) |
             ((FundingContributor.status.is_null()) |
              (FundingContributor.status.contains("sent").__invert__())))).join(
                  FundingRecord, on=(Task.id == FundingRecord.task_id)).join(
                      FundingContributor,
                      on=(FundingRecord.id == FundingContributor.funding_record_id)).join(
                          User,
                          JOIN.LEFT_OUTER,
                          on=((User.email == FundingContributor.email) |
                              (User.orcid == FundingContributor.orcid)))
             .join(Organisation, JOIN.LEFT_OUTER, on=(Organisation.id == Task.org_id)).join(
                 UserInvitation,
                 JOIN.LEFT_OUTER,
                 on=((UserInvitation.email == FundingContributor.email)
                     & (UserInvitation.task_id == Task.id))).join(
                         OrcidToken,
                         JOIN.LEFT_OUTER,
                         on=((OrcidToken.user_id == User.id)
                             & (OrcidToken.org_id == Organisation.id)
                             & (OrcidToken.scope.contains("/activities/update")))).limit(20))

    for (task_id, org_id, funding_record_id, user), tasks_by_user in groupby(tasks, lambda t: (
            t.id,
            t.org_id,
            t.funding_record.id,
            t.funding_record.funding_contributor.user,)):
        utils.create_or_update_funding(user=user, org_id=org_id, records=tasks_by_user)
    funding_contributor = FundingContributor.get(orcid=12344)
    assert 12399 == funding_contributor.put_code
    assert "12344" == funding_contributor.orcid


@patch("orcid_hub.orcid_client.MemberAPI.create_or_update_affiliation", side_effect=create_or_update_fund_or_aff_mock)
@patch("orcid_hub.orcid_client.MemberAPI.get_record", side_effect=get_record_mock)
def test_create_or_update_affiliation(patch, test_db, request_ctx):
    """Test create or update affiliation."""
    org = Organisation(
        name="THE ORGANISATION",
        tuakiri_name="THE ORGANISATION",
        confirmed=True,
        orcid_client_id="APP-5ZVH4JRQ0C27RVH5",
        orcid_secret="Client Secret",
        city="CITY",
        country="COUNTRY",
        disambiguation_org_id="ID",
        disambiguation_org_source="SOURCE")
    org.save()

    u = User(
        email="test1234456@mailinator.com",
        name="TEST USER",
        username="test123",
        roles=Role.RESEARCHER,
        orcid="123",
        confirmed=True,
        organisation=org)
    u.save()
    user_org = UserOrg(user=u, org=org)
    user_org.save()

    t = Task(
        org=org,
        filename="xyz.json",
        created_by=u,
        updated_by=u,
        task_type=0)
    t.save()

    af = AffiliationRecord(
        is_active=True,
        task=t,
        external_id="Test",
        first_name="Test",
        last_name="Test",
        email="test1234456@mailinator.com",
        orcid="123112311231",
        organisation="asdasd",
        affiliation_type="staff",
        role="Test",
        department="Test",
        city="Test",
        state="Test",
        country="Test",
        disambiguated_id="Test",
        disambiguated_source="Test")
    af.save()

    ui = UserInvitation(
        invitee=u,
        inviter=u,
        org=org,
        task=t,
        email="test1234456@mailinator.com",
        token="xyztoken")
    ui.save()

    ot = OrcidToken(
        user=u,
        org=org,
        scope="/read-limited,/activities/update",
        access_token="Test_token")
    ot.save()

    tasks = (Task.select(
        Task, AffiliationRecord, User, UserInvitation.id.alias("invitation_id"), OrcidToken).where(
            AffiliationRecord.processed_at.is_null(), AffiliationRecord.is_active,
            ((User.id.is_null(False) & User.orcid.is_null(False) & OrcidToken.id.is_null(False)) |
             ((User.id.is_null() | User.orcid.is_null() | OrcidToken.id.is_null()) &
              UserInvitation.id.is_null() &
              (AffiliationRecord.status.is_null()
               | AffiliationRecord.status.contains("sent").__invert__())))).join(
                   AffiliationRecord, on=(Task.id == AffiliationRecord.task_id)).join(
                       User,
                       JOIN.LEFT_OUTER,
                       on=((User.email == AffiliationRecord.email) |
                           (User.orcid == AffiliationRecord.orcid))).join(
                               Organisation, JOIN.LEFT_OUTER, on=(Organisation.id == Task.org_id))
             .join(
                 UserInvitation,
                 JOIN.LEFT_OUTER,
                 on=((UserInvitation.email == AffiliationRecord.email) &
                     (UserInvitation.task_id == Task.id))).join(
                         OrcidToken,
                         JOIN.LEFT_OUTER,
                         on=((OrcidToken.user_id == User.id) &
                             (OrcidToken.org_id == Organisation.id) &
                             (OrcidToken.scope.contains("/activities/update")))).limit(20))
    for (task_id, org_id, user), tasks_by_user in groupby(tasks, lambda t: (
            t.id,
            t.org_id,
            t.affiliation_record.user, )):
        utils.create_or_update_affiliations(user=user, org_id=org_id, records=tasks_by_user)
    affiliation_record = AffiliationRecord.get(task=t)
    assert 12399 == affiliation_record.put_code
    assert "12344" == affiliation_record.orcid
    assert "Employment record was created" in affiliation_record.status
