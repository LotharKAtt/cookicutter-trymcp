#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import io
import sys
import yaml

from cookiecutter.main import cookiecutter


def read_ctx_file(config_file):
    with io.open(config_file, encoding='utf-8') as file_handle:
        yaml_string = file_handle.read()
        try:
            yaml_dict = yaml.load(yaml_string)
        except Exception as e:
            msg = 'Error: Could not load config YAML file.\n%s' % e
            print(msg, file=sys.stderr)
            sys.exit(1)

    return yaml_dict.get('default_context', {})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--template',
                        required=True,
                        help='path to cookiecutter template')
    parser.add_argument('--config-file',
                        help='path to YAML config file')
    parser.add_argument('--output-dir',
                        help='path to output model')
    args = parser.parse_args()
    template = args.template
    config_file = args.config_file
    extra_context = read_ctx_file(config_file) if config_file else {}
    output_dir = args.output_dir or '.'

    cookiecutter(
        template,
        extra_context=extra_context,
        output_dir=output_dir,
        no_input=True,
        overwrite_if_exists=True
    )
