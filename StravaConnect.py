import requests

class StravaObject(object):
    def __init__(self, api_token, endpoint=''):
        self.base_url = "https://www.strava.com/api/v3/"
        self.api_token = api_token
        self.endpoint = endpoint
        
    def get(self, *args):
        headers = {}
        headers["Authorization"] = f"Bearer {self.api_token}"
        url = self.base_url + self.endpoint + '/'.join(args)

        try:
            resp = requests.get(url, headers=headers)
            assert(resp.status_code == 200)
        except:
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
        resp = self.get('athlete')
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
        raise NotImplementedError
        
    def getStats(self):
        raise NotImplementedError