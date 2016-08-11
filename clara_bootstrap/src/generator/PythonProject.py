# coding=utf-8

from clara_bootstrap.src.utils.SystemUtils import *
from clara_bootstrap.src.res.BaseConstants import LICENSE, GITIGNORE, README


def _package_folder(project_name):
    return project_name + "/" + project_name + "/"


def _test_folder(project_name):
    return project_name + "/tests/"


def create_init_file(path, template=None):
    init_file_path = path + "__init__.py"
    if template:
        create_file_from_template(init_file_path, template, )
    else:
        create_file_from_string(init_file_path)


def create_python_service(project_name):
    service_name = project_name + "Service"
    service_file_path = _package_folder(project_name) + service_name + ".py"
    test_file_path = _test_folder(project_name) + "test_" + service_name + ".py"

    # Create the service
    create_file_from_template(service_file_path,
                              "services/python.txt",
                              service_name=service_name)

    # Create tests
    create_file_from_template(test_file_path,
                              "services/python_test.txt",
                              project_name=project_name)


def create_python_setup(project_name):
    setup_file_path = project_name + "/setup.py"

    # Create setup.py
    create_file_from_template(setup_file_path,
                              "setup/python_setup.txt",
                              project_name=project_name)
    make_executable(setup_file_path)


def create_root_dir(project_name):
    # Create project folder
    create_folder(_package_folder(project_name))
    create_folder(_test_folder(project_name))

    # Create __init__.py
    create_file_from_template(_package_folder(project_name) +
                              "__init__.py", "services/python_init.txt",
                              author=get_username())
    create_file_from_string(_test_folder(project_name) + "__init__.py")

    # README.md
    create_file_from_string(project_name + "/README.md", README)
    # LICENSE
    create_file_from_string(project_name + "/LICENSE", LICENSE)
    # .gitignore
    create_file_from_string(project_name + "/.gitignore", GITIGNORE)


def create_python_project(project_name):

    if project_name:
        print "Creating the CLARA project skeleton..."
        create_root_dir(project_name)
        create_python_setup(project_name)
        create_python_service(project_name)
        print "Project created."

    else:
        raise Exception("Project name is required for scaffolding...")
