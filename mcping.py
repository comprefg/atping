from mcstatus import JavaServer


server = JavaServer.lookup("185.107.194.138:33711")


status = server.status()
print(f"The server has {status.players.online} player(s) online and replied in {status.latency} ms")

latency = server.ping()
print(f"The server replied in {latency} ms")

query = server.query()
print(f"The server has the following players online: {', '.join(query.players.names)}")
