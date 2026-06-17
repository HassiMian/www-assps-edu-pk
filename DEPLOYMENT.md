# Deployment Notes

## Production Mapping

- Domain: `www.assps.edu.pk`
- Server web root: `/var/www/apex-web`

## Current Behavior

- `assps.edu.pk` redirects to `www.assps.edu.pk`
- Static files are served from `/var/www/apex-web`
- API traffic goes to backend `127.0.0.1:5000`

## Safety

- GitHub pushes do not deploy automatically.
- Live deployment should be done separately and carefully.

