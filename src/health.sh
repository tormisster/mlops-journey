#!/usr/bin/env bash
echo "python: $(python3 --version)"
echo "disk:   $(df -h . | tail -1 | awk '{print $4}') free"
