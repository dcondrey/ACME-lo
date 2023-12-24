#!/bin/bash

# Set environment variables
export ACME_LO_ENV="development"
export DATABASE_URL="postgresql://username:password@localhost/acme_lo_db"

# Load environment variables from a file (optional)
# source .env

# Configure database connection
# Example: Start a PostgreSQL database server
# service postgresql start

echo "Environment configured successfully"

