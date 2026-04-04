
if [ -z "$1" ]; then
    echo "Usage: ./scripts/push.sh \"Your commit message here\""
    exit 1
fi
git add .
git commit -m "$1"
git push -u origin main