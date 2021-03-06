from distutils.core import setup

setup(
    name = "django-la-facebook",
    version = "0.1.0",
    author = "pydanny",
    author_email = "pydanny@pydanny.com",
    description = "Definitive facebook auth for Django",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/cartwheelweb/django-la-facebook",
    packages = [
        "la_facebook",
        "la_facebook.templatetags",
        "la_facebook.utils",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
