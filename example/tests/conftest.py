import os
import uuid

from pathlib import Path
from typing import Callable

import pytest

from mountebank_mocks_manager.manager import MocksManager


root_path = Path(__file__).parent.parent.resolve()
imposters_root = root_path / 'imposters'

mb_server_host = os.getenv('MOUNTEBANK_HOST', '127.0.0.1')
mb_server_port = int(os.getenv('MOUNTEBANK_PORT', '2525'))
bob_port = int(os.getenv('BOB_PORT', '50518'))


services = {'bob': {'name': 'bob', 'port': bob_port}}


def pytest_sessionstart(session):
    session.is_parallel = hasattr(session.config, 'workerinput')

    if session.is_parallel:
        session.worker_id = session.config.workerinput.get('workerid', 'gw0')
    else:
        session.worker_id = 'master'

    session.is_master = session.worker_id in ('master', 'gw0')


@pytest.fixture(scope='session')
def is_parallel(request):
    return request.session.is_parallel


@pytest.fixture(scope='function')
def session_id():
    yield str(uuid.uuid4())


@pytest.fixture(scope='function')
def mocks_manager(request, session_id) -> MocksManager:
    imposters_root = root_path / 'imposters'
    return MocksManager(
        request=request,
        imposters_root=imposters_root,
        session_id=session_id,
        parallel=request.session.is_parallel,
        mb_server_host=mb_server_host,
        mb_server_port=mb_server_port,
        services=services,
    )


@pytest.fixture(scope='function')
def mocks_group(request, mocks_manager: MocksManager, session_id) -> Callable:
    request.session.session_id = session_id
    return mocks_manager.mocks_group
