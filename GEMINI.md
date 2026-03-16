# Document the network / server topology of blueszeppelin.net

Document the network, proxy, server and application layout of the "blueszeppelin.net" podcast.

## Sources

- Document the server software, the links, proxy and publishing places
- Trace the chain back from https://podcasts.apple.com/ca/podcast/the-blueszeppelin-hosted-by-mark-stenzler-has-been/id1046574635
- Follow all links from https://blueszeppelin.net
- Have a look at https://blueszeppelin.net/podcast

## Documentation
- Keep all infos in the README.md
- Maintain a `roadmap.md` file to track the next 5 tasks and overall progress
  - Before executing a task from the roadmap, check if it is really already done
- Add embedded diagramms with plantuml, keep the diagram source in /diagrams
- Use tables instead of enumerations where several similar items are affected.

### Servers
- Document all servers with their function, redirects, ports, including itunes, rabe, youtube music
- Document all server with name, source, ip-addresses and status on port 443 and 80 with Emojis (update on each run)
- Include at least Apple, Youtube, feedburner, rabe, blueszeppelin and nuxit

### Software
- Document all systems with name, source, version, security flaws and available upgrades as a table
- Sort the layers from application down to OS/metall

### DNS
- Document the entire DNS configuration as a table, including responsible NS server and all entries with their function

