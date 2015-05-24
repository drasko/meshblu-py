import requests, json

class MeshbluRestClient():
    """
        Class that implements Meshblu client API via RESTful calls
    """

    def __init__(self):
        self.url = 'http://meshblu.octoblu.com'


    ###
    # STATUS
    ###
    def getStatus(self):
        """
            Returns the Meshblu platform status.
        """
        r = requests.get(self.url + '/status')
        print r.text
        return r.json()


    ###
    # DEVICE
    ###
    def addDevice(self, data):
        """
            Payload: key=value (i.e. type=drone&color=black)
            Registers a node or device with Meshblu. Meshblu returns
            a UUID device id and security token.
            You can pass any key/value pairs and even override Meshblu's
            auto-generated UUID and/or token by passing your own uuid and/or
            token in the payload i.e. uuid=123&token=456.
        """
        r = requests.post(self.url + '/devices')

    def getDevices(self, data):
        """
            Returns an array of device UUIDs based on key/value query criteria.
        """
        r = requests.get(self.url + '/devices')
        print r.text
        return r.json()

    def getDevice(self, uuid):
        """
            Returns all information (except the token) of a specific device or node.
        """
        r = requests.get(self.url + '/devices/' + uuid)
        print r.text
        return r.json()

    def getDeviceKey(self, uuid):
        """
            Returns the base64-encoded public key for the device,
            or null if the device does not have a public key.
        """
        r = requests.get(self.url + '/devices/' + uuid + '/publickey')
        print r.text
        return r.json()

    def getDeviceToken(self, uuid):
        """
            Returns a new session token for the device
        """
        r = requests.post(self.url + '/devices/' + uuid + '/tokens')
        print r.text
        return r.json()

    def updateDevice(self, uuid, data):
        """
            Updates a node or device currently registered with Meshblu
            that you have access to update.
            You can pass any key/value pairs to update object as well as
            null to remove a propery (i.e. color=null).
        """
        r = requests.post(self.url + '/devices/' + uuid)
        print r.text
        return r.json()

    def deleteDevice(self, uuid):
        """
            Deletes or unregisters a node or device currently registered
            with Meshblu that you have access to update.
        """
        r = requests.delete(self.url + '/devices/' + uuid)
        print r.text
        return r.json()


    ###
    # LOCALDEVICES
    ###
    def getLocalDevices(self):
        """
            Returns a list of unclaimed devices that are on the
            same network as the requesting resource.
        """
        r = requests.get(self.url + '/localdevices')
        print r.text
        return r.json()


    ###
    # CLAIMDEVICE
    ###
    def claimDevice(self, uuid):
        """
            Adds the `meshblu_auth_uuid` as the owner of this device UUID
            allowing a user or device to claim ownership of another device.
        """
        r = requests.put(self.url + '/claimdevice/:' + uuid)
        print r.text
        return r.json()


    ###
    # MYDEVICES
    ###
    def getMyDevices(self):
        """
            Returns all information (including tokens) of all devices or
            nodes belonging to a user's UUID
            (identified with an "owner" property and user's UUID,
             i.e. "owner":"0d1234a0-1234-11e3-b09c-1234e847b2cc").
        """
        r = requests.get(self.url + '/mydevices')
        print r.text
        return r.json()


    ###
    # MESSAGES
    ###
    def sendMessage(self, data):
        """
            Send a message to a specific device, array of devices,
            or all devices subscribing to a UUID on the Meshblu platform.
        """
        r = requests.post(self.url + '/messages')
        print r.text
        return r.json()


    ###
    # EVENTS
    ###
    def getEvents(self, uuid):
        """
            Returns last 10 events related to a specific device or node.
        """
        r = requests.get(self.url + '/events' + uuid)
        print r.text
        return r.json()


    ###
    # SUBSCRIBE
    ###
    def subscribe(self):
        """
            This is a streaming API that returns device/node messages as
            they are sent and received. Notice the comma at the end of
            the response. Meshblu doesn't close the stream.
        """
        r = requests.get(self.url + '/subscribe')
        print r.text
        return r.json()

    def subscribeBroadcast(self, uuid):
        """
            This is a streaming API that returns device/node broadcasts
            messages as they are sent. Notice the comma at the
            end of the response. Meshblu doesn't close the stream.

            Note: This will stream broadcast messages from the uuid you've specified.
            The uuid/token you're authenticating with must have permissions to
            view messages from the subscribed uuid.
        """
        r = requests.get(self.url + '/subscribe/' + uuid)
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
    def setData(self, uuid, data):
        """
            Stores sensor data for a particular UUID. You can pass any key/value pairs.
        """
        r = requests.post(self.url + '/data/' + uuid)
        print r.text
        return r.json()

    def getData(self, uuid):
        """
            Returns last 10 data updates related to a specific device or node
            Optional query parameters include: start (time to start from),
            finish (time to end), limit (overrides the default 10 updates).

            Note: You can make this API stream sensor data by adding stream=true
            to the querystring. Notice the comma at the end of the response.
            Meshblu doesn't close the stream.
        """
        r = requests.get(self.url + '/data/' + uuid)
        print r.text
        return r.json()
