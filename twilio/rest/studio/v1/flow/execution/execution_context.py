# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ExecutionContextList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, flow_sid, execution_sid):
        """
        Initialize the ExecutionContextList

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.
        :param execution_sid: Execution Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextList
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextList
        """
        super(ExecutionContextList, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, }

    def get(self):
        """
        Constructs a ExecutionContextContext

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        return ExecutionContextContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
        )

    def __call__(self):
        """
        Constructs a ExecutionContextContext

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        return ExecutionContextContext(
            self._version,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionContextList>'


class ExecutionContextPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the ExecutionContextPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param flow_sid: Flow Sid.
        :param execution_sid: Execution Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextPage
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextPage
        """
        super(ExecutionContextPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ExecutionContextInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        return ExecutionContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionContextPage>'


class ExecutionContextContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, flow_sid, execution_sid):
        """
        Initialize the ExecutionContextContext

        :param Version version: Version that contains the resource
        :param flow_sid: Flow Sid.
        :param execution_sid: Execution Sid.

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        super(ExecutionContextContext, self).__init__(version)

        # Path Solution
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, }
        self._uri = '/Flows/{flow_sid}/Executions/{execution_sid}/Context'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ExecutionContextInstance

        :returns: Fetched ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ExecutionContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionContextContext {}>'.format(context)


class ExecutionContextInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, flow_sid, execution_sid):
        """
        Initialize the ExecutionContextInstance

        :returns: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        super(ExecutionContextInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'context': payload['context'],
            'flow_sid': payload['flow_sid'],
            'execution_sid': payload['execution_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'flow_sid': flow_sid, 'execution_sid': execution_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ExecutionContextContext for this ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextContext
        """
        if self._context is None:
            self._context = ExecutionContextContext(
                self._version,
                flow_sid=self._solution['flow_sid'],
                execution_sid=self._solution['execution_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def context(self):
        """
        :returns: Flow state.
        :rtype: dict
        """
        return self._properties['context']

    @property
    def flow_sid(self):
        """
        :returns: Flow Sid.
        :rtype: unicode
        """
        return self._properties['flow_sid']

    @property
    def execution_sid(self):
        """
        :returns: Execution Sid.
        :rtype: unicode
        """
        return self._properties['execution_sid']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a ExecutionContextInstance

        :returns: Fetched ExecutionContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_context.ExecutionContextInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionContextInstance {}>'.format(context)
