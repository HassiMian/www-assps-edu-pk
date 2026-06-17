# www.assps.edu.pk

Public website for ASSPS.

## Domain

- Production: `https://www.assps.edu.pk`
- Redirect source: `https://assps.edu.pk`

## Local Snapshot Source

- Original workspace source: `c:\projects\My SAas\apex-web`

## Live Server Mapping

- Nginx web root: `/var/www/apex-web`
- Static site served directly by Nginx
- `/api/` requests proxy to backend on `127.0.0.1:5000`

## Local Use

- this is a static site snapshot
- you can preview it with any simple static file server
- older repair/screenshot helpers are stored under `ops/legacy/`

## Notes

- This repository was split safely from the larger workspace.
- Creating or updating this repository does not change the live site unless a separate deployment step is run.

See [ARCHITECTURE.md](ARCHITECTURE.md).
