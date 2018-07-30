import openstack


def create_connection(auth_url, project_name, username, password, region, project_domain_id, user_domain_id):

    conn = openstack.connection.Connection(auth_url=auth_url, project_name=project_name, username=username, password=password, region=region, project_domain_id=project_domain_id, user_domain_id=user_domain_id)
    return conn
