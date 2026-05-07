import requests

URL = "https://roadmap.sh/api/v1-official-roadmap/frontend"

response = requests.get(URL)

# cek request berhasil
response.raise_for_status()

data = response.json()

nodes = data.get("nodes", [])

# urutkan berdasarkan posisi visual
sorted_nodes = sorted(
    nodes,
    key=lambda n: (
        n.get("position", {}).get("y", 0),
        n.get("position", {}).get("x", 0)
    )
)

print(f"Total nodes: {len(sorted_nodes)}\n")

for node in sorted_nodes:
    node_type = node.get("type")

    # ambil label/title
    label = (
        node.get("data", {}).get("label")
        or node.get("title")
        or "-"
    )

    x = node.get("position", {}).get("x")
    y = node.get("position", {}).get("y")

    print(f"""
Type  : {node_type}
Label : {label}
X,Y   : ({x}, {y})
ID    : {node.get("id")}
""")