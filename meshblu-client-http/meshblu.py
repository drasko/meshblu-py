import requests, json
import sys

class MeshbluRestClient():
    """
        Class that implements Meshblu client API via RESTful calls
    """

    def __init__(self, url):
        self.url = url
        self.authUuid = ''
        self.token = ''

    def setCredentials(self, authUuid, token):
        self.authUuid = authUuid
        self.token = token

    def getHeaders(self, authUuid, token):
        """
            Set-up the heades that will be sent with HTTP requests
        """
        if ( (authUuid is not None) and (token is None) ) or ( (authUuid is None) and (token is not None) ):
            print "HEADERS: Wrong params - if authUuid or token is used, both values must be provided"
            # Zero-init the params not to break the current thread - although the result will be wrong
            authUuid = ''
            token = ''

        if (authUuid is None and token is None):
            authUuid = self.authUuid
            token = self.token

        headers = headers = {'meshblu_auth_uuid':authUuid, 'meshblu_auth_token':token}
        return headers


    ###
    # STATUS
    ###
    def getStatus(self):
        """
            Returns the Meshblu platform status.
        """
        r = requests.get(self.url + '/status')
        return r.json()


    ###
    # DEVICE
    ###
    def addDevice(self, payload, authUuid=None, token=None):
        """
            Payload: key=value (i.e. type=drone&color=black)
            Registers a node or device with Meshblu. Meshblu returns
            a UUID device id and security token.
            You can pass any key/value pairs and even override Meshblu's
            auto-generated UUID and/or token by passing your own uuid and/or
            token in the payload i.e. uuid=123&token=456.
        """
        if (authUuid is not None and token is not None):
            payload = payload.update({'meshblu_auth_uuid':authUuid, 'meshblu_auth_token':token})

        r = requests.post(self.url + '/devices', params=payload)
        return r.json()

    def getDevices(self, payload, authUuid=None, token=None):
        """
            Returns an array of device UUIDs based on key/value query criteria.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/devices', params=payload, headers=headers)
        return r.json()

    def getDevice(self, uuid, authUuid=None, token=None):
        """
            Returns all information (except the token) of a specific device or node.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/devices/' + uuid, headers=headers)
        return r.json()

    def getDeviceKey(self, uuid):
        """
            Returns the base64-encoded public key for the device,
            or null if the device does not have a public key.
        """
        r = requests.get(self.url + '/devices/' + uuid + '/publickey')
        print r.text
        return r.json()

    def getDeviceToken(self, uuid, authUuid=None, token=None):
        """
            Returns a new session token for the device
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.post(self.url + '/devices/' + uuid + '/tokens', headers=headers)
        print r.text
        return r.json()

    def updateDevice(self, uuid, payload, authUuid=None, token=None):
        """
            Updates a node or device currently registered with Meshblu
            that you have access to update.
            You can pass any key/value pairs to update object as well as
            null to remove a propery (i.e. color=null).
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.put(self.url + '/devices/' + uuid, params=payload, headers=headers)
        print r.text
        return r.json()

    def deleteDevice(self, uuid, authUuid=None, token=None):
        """
            Deletes or unregisters a node or device currently registered
            with Meshblu that you have access to update.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.delete(self.url + '/devices/' + uuid, headers=headers)
        print r.text
        return r.json()


    ###
    # LOCALDEVICES
    ###
    def getLocalDevices(self, authUuid=None, token=None):
        """
            Returns a list of unclaimed devices that are on the
            same network as the requesting resource.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/localdevices', headers=headers)
        print r.text
        return r.json()


    ###
    # CLAIMDEVICE
    ###
    def claimDevice(self, uuid, authUuid=None, token=None):
        """
            Adds the `meshblu_auth_uuid` as the owner of this device UUID
            allowing a user or device to claim ownership of another device.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.put(self.url + '/claimdevice/' + uuid, headers=headers)
        print r.text
        return r.json()


    ###
    # MYDEVICES
    ###
    def getMyDevices(self, authUuid=None, token=None):
        """
            Returns all information (including tokens) of all devices or
            nodes belonging to a user's UUID
            (identified with an "owner" property and user's UUID,
             i.e. "owner":"0d1234a0-1234-11e3-b09c-1234e847b2cc").
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/mydevices', headers=headers)
        print r.text
        return r.json()


    ###
    # MESSAGES
    ###
    def sendMessage(self, payload, authUuid=None, token=None):
        """
            Send a message to a specific device, array of devices,
            or all devices subscribing to a UUID on the Meshblu platform.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.post(self.url + '/messages', params=payload, headers=headers)
        print r.text
        return r.json()


    ###
    # EVENTS
    ###
    def getEvents(self, uuid, authUuid=None, token=None):
        """
            Returns last 10 events related to a specific device or node.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/events' + uuid, headers=headers)
        print r.text
        return r.json()


    ###
    # SUBSCRIBE
    ###
    def subscribe(self, authUuid=None, token=None):
        """
            This is a streaming API that returns device/node messages as
            they are sent and received. Notice the comma at the end of
            the response. Meshblu doesn't close the stream.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/subscribe', headers=headers)
        print r.text
        return r.json()

    def subscribeBroadcast(self, uuid, authUuid=None, token=None):
        """
            This is a streaming API that returns device/node broadcasts
            messages as they are sent. Notice the comma at the
            end of the response. Meshblu doesn't close the stream.

            Note: This will stream broadcast messages from the uuid you've specified.
            The uuid/token you're authenticating with must have permissions to
            view messages from the subscribed uuid.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/subscribe/' + uuid, headers=headers)
        print r.text
        return r.json()


    ###
    # IPADDRESS
    ###
    def getIpAddr(self):
        """
            Returns the public IP address of the request.
            This is useful when working with the Meshblu Gateway behind a firewall.
        """
        r = requests.get(self.url + '/ipaddress')
        print r.text
        return r.json()


    ###
    # DATA
    ###
    def setData(self, uuid, payload, authUuid=None, token=None):
        """
            Stores sensor data for a particular UUID. You can pass any key/value pairs.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.post(self.url + '/data/' + uuid, params=payload, headers=headers)
        print r.text
        return r.json()

    def getData(self, uuid, authUuid=None, token=None):
        """
            Returns last 10 data updates related to a specific device or node
            Optional query parameters include: start (time to start from),
            finish (time to end), limit (overrides the default 10 updates).

            Note: You can make this API stream sensor data by adding stream=true
            to the querystring. Notice the comma at the end of the response.
            Meshblu doesn't close the stream.
        """
        headers = self.getHeaders(authUuid, token)
        r = requests.get(self.url + '/data/' + uuid, headers=headers)
        print r.text
        return r.json()
