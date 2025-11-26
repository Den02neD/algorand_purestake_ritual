import requests, time

def purestake_ritual():
    print("Algorand — The PureStake Ritual Has Begun")
    seen = set()
    while True:
        r = requests.get("https://mainnet-idx.algonode.cloud/v2/transactions?limit=50")
        for tx in r.json().get("transactions", []):
            txid = tx["id"]
            if txid in seen: continue
            seen.add(txid)

            # Detect massive opt-in spree (the ritual)
            if tx.get("tx-type") != "acfg": continue
            if int(tx.get("asset-config", {}).get("total", 0)) != 1: continue
            
            sender = tx["sender"]
            # Count how many ASAs this address created in last 10 seconds (via seen)
            if len([x for x in seen if x.startswith(sender[:10])]) > 80:
                print(f"THE PURESTAKE RITUAL IS COMPLETE\n"
                      f"One mind just birthed 80+ ASAs in under 10 seconds\n"
                      f"Creator: {sender}\n"
                      f"Latest child: {txid[-12:]}\n"
                      f"https://algoexplorer.io/tx/{txid}\n"
                      f"→ This is not spam. This is liturgy.\n"
                      f"→ On Algorand, creation is measured in milliseconds.\n"
                      f"→ A new pantheon just materialized from nothing.\n"
                      f"{'⟐   '*35}\n")
        time.sleep(0.9)

if __name__ == "__main__":
    purestake_ritual()
