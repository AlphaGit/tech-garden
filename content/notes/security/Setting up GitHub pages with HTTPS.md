---
title: Setting up GitHub pages with HTTPS
tags:
- ssl
- github
- github pages
- dns
---

I had a particular case for this tech garden while setting up [[SSL]]:

- **My domain was not an apex domain.** This means: it was a subdomain. Instead of `alphasmanifest.com`,  I wanted to use `techgarden.alphasmanifesto.com`
- **My github repository is not a direct association to my user.** This means: instead of `AlphaGit/alphagit.github.io`, my repository was `AlphaGit/tech-garden`.

With all of this, I struggled a bit to make HTTPS work but here's how to set itup:

1. In your [[DNS]] provider, setup your subdomain to have a `CNAME` record matching your base GitHub publishing domain. This would be `<yourUser>.github.io` or `<yourOrganization>.github.io`. It doesn't matter if you're using another repo, don't add anything else to it.
   ![[notes/security/Route53 CNAME Example.png|400]]
2. Make sure that the changes are propagated.
3. In GitHub pages, publish your site.
4. Associate a custom domain to it, using the subdomain you setup. In my case: `techgarden.alphasmanifesto.com`
   ![[notes/security/Github pages custom domain.png]]
5. Click on Save. This will create a `CNAME` file in your repo, in the publishing folder you selected. It will also validate the configuration of your DNS records.
6. If allowed, click on Enforce HTTPS. *It might fail*, but wait at least one hour. It does work even if it reports an error at first.

You're looking at that result right now.