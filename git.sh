git init
git add .
git commit -m "initial commit: io_helpers package (pyarrow/pyiceberg/sparkiceberg/sparkdelta/deltalake write helpers + shared schema guards)"
gh repo create helper_io_helpers --public --source=. --remote=origin --push

git remote -v
gh repo view --web
