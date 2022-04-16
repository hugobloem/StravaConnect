import requests
import logging as log

log.basicConfig(level=log.DEBUG)

from aiohttp import ClientSession, ClientResponse


class Auth:
    """Class to make authenticated requests."""

    def __init__(self, websession: ClientSession, host: str, access_token: str):
        """Initialize the auth."""
        self.websession = websession
        self.host = host
        self.access_token = access_token

    async def request(self, method: str, path: str, **kwargs) -> ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        headers["authorization"] = self.access_token

        return await self.websession.request(
            method, f"{self.host}/{path}", **kwargs, headers=headers,
        )

class StravaObject(object):
    def __init__(self, api_token, endpoint=''):
        self.base_url = "https://www.strava.com/api/v3/"
        self.api_token = api_token
        self.endpoint = endpoint

        async with aiohttp.ClientSession() as session:
            self.auth = Auth(session, self.base_url, "1bae07847760d10f1919bede2c8286181c13cb58" )

    def get(self, *args):
        headers = {}
        headers["Authorization"] = f"Bearer {self.api_token}"
        url = self.base_url + self.endpoint + '/' + '/'.join(args)

        try:
            log.debug(url)
            resp = await auth.request("get", "lights")
            print("HTTP response status code", resp.status)
            print("HTTP response JSON content", await resp.json())
            assert(resp.status_code == 200)
        except:
            log.debug(resp.text)
            raise Warning(f"Could not get requested object at {self.endpoint}")

        return resp.json()


class Strava(StravaObject):

    def GetAthlete(self):
        self.athlete = Athlete(self.api_token)


class Activities(StravaObject):
    def __init__(self, api_token):
        super().__init__(api_token, 'activities')

    def getActivityById(self):
        return self.get('activities', 'id')

    def getCommentsByActivityId(self):
        raise NotImplementedError

    def getKudoersByActivityId(self):
        raise NotImplementedError

    def getLapsByActivityId(self):
        raise NotImplementedError

    def getLoggedInAthleteActivities(self):
        raise NotImplementedError

    def getZonesByActivityId(self):
        raise NotImplementedError


class Athlete(StravaObject):
    def __init__(self, api_token):
        super().__init__(api_token, 'athlete')
        
        self.getLoggedInAthlete()

    def getLoggedInAthlete(self):
        resp = self.get()
        self.uid = resp['id']
        self.username = resp['username']
        self.resource_state = resp['resource_state']
        self.firstname = resp['firstname']
        self.lastname = resp['lastname']
        self.bio = resp['bio']
        self.city = resp['city']
        self.state = resp['state']
        self.country = resp['country']
        self.sex = resp['sex']
        self.premium = resp['premium']
        self.summit = resp['summit']
        self.created_at = resp['created_at']
        self.updated_at = resp['updated_at']
        self.badge_type_id = resp['badge_type_id']
        self.weight = resp['weight']
        self.profile_medium = resp['profile_medium']
        self.profile = resp['profile']
        self.friend = resp['friend']
        self.follower = resp['follower']

    def getLoggedInAthleteZones(self):
        resp = self.get('zones')
        self.zones = resp
        
    def getStats(self):
        raise NotImplementedError