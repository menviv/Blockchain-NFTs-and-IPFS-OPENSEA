
from brownie import AdvancedNFT, config, network
from scripts.helpful_scripts import BREED_MAPPING, get_account, OPENSEA_URL, LOCAL_BLOCKCHAIN_ENVIRONMENTS,getBreed
from metadata.sample import metadata_template
from web3 import Web3
from pathlib import Path
import requests
import json
import os


breed_to_image_uri = {
    "k1": "https://ipfs.io/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH?filename=0-k1.json",
    "k2": "https://ipfs.io/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH?filename=2-k2.json",
    "k3": "https://ipfs.io/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH?filename=1-k3.json"
}

def main():
    collection = AdvancedNFT[-1]
    number_of_nfts = collection.tokenCounter()
    print(f"You have created {number_of_nfts} nts")
    for token_id in range(number_of_nfts):
        breed = getBreed(collection.tokenIdBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        print(metadata_file_name)
        collectionMeta = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists..")
        else:
            print(f"creating {metadata_file_name}")
            collectionMeta["name"] = breed
            collectionMeta["description"] = f"an adorable {breed} bird!"
            image_file_path = f"./img/{breed}.jpg"
            print(image_file_path)
            image_uri = None
            if os.getenv("UPLOAD_TO_IPFS")=="true":
                image_uri = upload_to_ipfs(image_file_path)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]
            collectionMeta["image"] = image_uri
            with Path(metadata_file_name).open("w") as file:
                json.dump(collectionMeta, file)
                if os.getenv("UPLOAD_TO_IPFS")=="true":
                    upload_to_ipfs(metadata_file_name)




def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url="http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url+endpoint, files={"file": image_binary})
        print(response.json())
        ipfs_hash = response.json()["Hash"]
        # "./img/k2.jpg" => "k2.jpg"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
