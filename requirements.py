import pkg_resources

def check_requirements(requirements_file):
    with open(requirements_file, 'r') as file:
        required_packages = file.readlines()

    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

    for requirement in required_packages:
        if '==' in requirement:
            pkg_name, pkg_version = requirement.strip().split('==')
            if pkg_name in installed_packages:
                if installed_packages[pkg_name] != pkg_version:
                    print(f"{pkg_name} is installed with version {installed_packages[pkg_name]}, but version {pkg_version} is required.")
            else:
                print(f"{pkg_name} is not installed.")
        else:
            pkg_name = requirement.strip()
            if pkg_name not in installed_packages:
                print(f"{pkg_name} is not installed.")

check_requirements('requirements.txt')
