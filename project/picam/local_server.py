#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import argparse
import glob
import importlib
import uvicorn

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "community_prj.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
    parser = argparse.ArgumentParser(description='Summer local server runner')
    parser.add_argument('--module', help='root module name. optional.', type=str, default=None, required=False)
    parser.add_argument('--port', help='port, default 5000, optional.', type=int, default=5000, required=False)
    parser.add_argument('--no-reload',
                        help='disable automatic reload when a code changes. optional',
                        required=False,
                        action='store_true')
    args = parser.parse_args()
    module_name = args.module
    if not module_name:
        yml_path = 'config/properties.yml'
        module_name = None
        for d in filter(lambda f: os.path.isdir(f), glob.glob('*')):
            if os.path.isfile(f'{d}/{yml_path}'):
                module_name = d
                break

    module = importlib.import_module(module_name)
    getattr(module, 'create_app')

    reload = True if args.no_reload is None else False

    uvicorn.run(f'{module_name}:create_app', host='0.0.0.0', port=args.port, reload=reload)

