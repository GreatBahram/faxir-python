"""
    FAX.IR REST API

    This is the fax.ir API v2 developed for third party developers and organizations. In order to have a better coding experience with this API, let's quickly go through some points:<br /><br /> - This API assumes **/accounts** as an entry point with the base url of **https://api.fax.ir/v2**. <br /><br /> - This API treats all date and times sent to it in requests as **UTC**. Also, all dates and times returned in responses are in **UTC**<br /><br /> - Once you have an access_token, you can easily send a request to the resource server with the base url of **https://api.fax.ir/v2** to access your permitted resources. As an example to get the user's profile info you would send a request to **https://api.fax.ir/v2/accounts/self** when **Authorization** header is set to \"Bearer YOUR_ACCESS_TOKEN\" and custom header of **x-fax-clientid** is set to YOUR_CLIENT_ID  # noqa: E501
"""

import codecs

from setuptools import find_packages, setup  # noqa: H301

NAME = "faxir-api"
VERSION = "0.2.0"

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="FAX.IR REST API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="faxir",
    author_email="info@fax.ir",
    url="https://github.com/faxir/faxir-python",
    keywords=["faxir", "fax.ir", "atrisa"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Fax",
    ],
)
