#! /bin/bash
curl -X POST -H "Content-Type: application/json" \
          -d '{"title": "menu title 1", "description": "some description"}' \
          --verbose 'localhost:8000/api/v1/menus/'