"""Configuration loader"""
import yaml
import os

class ConfigLoader:
    def load(self, config_file="config/default.yaml"):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)
