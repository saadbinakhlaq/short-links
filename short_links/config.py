
import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'postgres')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'db')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'short_links_development')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'short_links_test')
