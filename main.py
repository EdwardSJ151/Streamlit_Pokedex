from subprocess import call


def run_webapp_main():
    call(["python", "pkdx_website_complete.py"])


def run_webapp_study():
    call(["python", "pkdx_study_website_complete.py"])


run_webapp_main()
