import requests
import json


wallet_addresses = [
    "0x00000000000000000000000000000000000000c7",
    "0x00000000000000000000000000000000000008b4",
    "0x0000000000000000000000000000000000000963",
    "0x0000000000000000000000000000000000000993",
    "0x00000000000000000000000000000000000009be",
    "0x0000000000000000000000000000000000000b7c",
    "0x0000000000000000000000000000000000000d78",
    "0x00000000000000000000000000000000000010f7",
    "0x000000000000000000000000000000000000139d",
    "0x0000000000000000000000000000000000001547",
    "0x000000000000000000000000000000000000155b",
    "0x000000000000000000000000000000000000291c",
    "0x000000000000000000000000000000000000363d",
    "0x00000000000000000000000000000000000036e3",
    "0x00000000000000000000000000000000000038c6",
    "0x0000000000000000000000000000000000004848",
    "0x00000000000000000000000000000000000085df",
    "0x000000000000000000000000000000000001e104",
    "0x000000000000000000000000000000000001ef23",
    "0x00000000000000000000000000000000000207ed",
    "0x0000000000000000000000000000000000021548",
    "0x0000000000000000000000000000000000021728",
    "0x0000000000000000000000000000000000021d79",
    "0x00000000000000000000000000000000000223ea",
    "0x00000000000000000000000000000000000234af",
    "0x000000000000000000000000000000000002749e",
    "0x00000000000a3ae1129ec96737bfc0f745767a70",
    "0x000000000014435de8dc7841fc0bc271a916d467",
    "0x0000000000b6339756c69614d183670ba8b25507",
    "0x0000000008a5f677d64163191f2fc3da269364b1",
    "0x000000006303ad2d5d2dc1114ea4a3eaee2d1c03",
    "0x000000062e42f23c963a0c5fd78424e83964bb25",
    "0x0000000fce96ad741238ddd445689ee77b89ac9e",
    "0x00000b46508882a135b4933b82a07df8f24a0068",
    "0x000016d58758f7f0debdef6c18ffc129a7c82017",
    "0x00002d30016ce16c4612f476195b2f0d796b5944",
    "0x000033cf33a3e2b342aa3c8b40eeedaed5706d35",
    "0x00006a71cc011b450e3c45508b9ab30ce4eb2ce4",
    "0x00008cb7b55d77b5116a593a67020603b7c07fd0",
    "0x0000ecb341a3c0bb394f377d3a524703fb8b76fb",
    "0x000101d1c9769ea22d6ea627b19bffcc99f61bf3",
    "0x0001778ca31414e9e6ff108d16d9a451525eb318",
    "0x0002c44aa9422390cd9cb066d64ba9d4359e08c5",
    "0x0003717bf8b1fc8cd97ecb6fffd59cb046b3c73e",
    "0x0003964c780dbdade65d9bb623e56d3e5aaaa5a1",
    "0x0003b4c9ccdefccfb0960930f6da15818afd4f76",
    "0x0003bfdccdfc8fc29df896dbe1aa384889d8d2e8",
    "0x0003f8283b9a5dfbec0b77a6603db55957345f07",
    "0x00056a21017477c5288759db76948bfdbe1c5ecf",
    "0x0005f9f9a8d7beef05da9dce69e8915f4f28bbb6",
    "0x0006809108ad27dc24fec9711d858782a833ba3e",
    "0x0006a7d3d625a468bcc5172fca5e41bfe0c1391c",
    "0x00081cc78f2b64b0e39e493845752d292c049b2e",
    "0x000851fb6b867eab6b3be75b4ac814c0378340ad",
    "0x0009b736831afa2fd0c6803b5d02ccbabb3e8e1a",
    "0x0009e6b6b45a639c96b3025604fd18c4ab89eaf8",
    "0x0009f9cbcfebe722bf40b3a2e3cad3c1a5c9d654",
    "0x000a027f6d4b7a34b0c7568503b96cb0ead48b8e",
    "0x000a159918e5168dd30c5f0600b507d058b94eec",
    "0x000b1a197fe80a3a9284ffbf118b8f4495877999",
    "0x000b1c65661dc8fc44fb18159aab09f352566d21",
    "0x000b21d4977ca864e4af8356d8d4215648c02a63",
    "0x000b5e83dd32ba4bab4b3d1744a73b36caaac715",
    "0x000bd87343a289cbdfb82e49704065247c56fd60",
    "0x000c2f509c5cf71613bf2b9f64cae5acef4ee85c",
    "0x000c3529e8bb86818fc350cdce4f77b730d0c7d4",
    "0x000ce63478185e24f64e0d845a8fdcb5288a0e9f",
    "0x000d704e800fc9582d15195813e0daaed9fa707c",
    "0x000e26b7d1af2abfb1312a534ecf3f65a73e99e5",
    "0x000e340b4640316d90d611cf0fb9eda6ba93c087",
    "0x000e7957dd0fb480a0639990813c883d10dd7276",
    "0x000e8b3b7028e6fe7f8d39c6c790cfef4513cd9c",
    "0x000f415db5d31528ec23363f3b3b978dc94b50c9",
    "0x000f6d0ccfa3e76ae5eb90d7f9e472c333d194e0",
    "0x000f98c6a03e192d0956a0f97f21d83bc9dfb75c",
    "0x000f9a40968c7b717a0fcbc859f9afa63bc4e6f9",
    "0x00103c9c5be9d7bb818b53763825c91c72808944",
    "0x00105a422a244a96a27aef7e96ad766f775bce88",
    "0x0010836e37858b8b4ed635d6f51a5fd8304b1cb4",
    "0x001096777e74308ef1c4857448e63c3be1a336cd",
    "0x0010ca154076fc72790407848ffe0cf3d9e34ca7",
    "0x00111590a11cc3dfd0e6a549c7e5da25bedc6557",
    "0x00118e982ccea7bd818a55138360f6894ac86522",
    "0x0011ad7e710d44763d5bd712aa79186713ba04fc",
    "0x00120ec799017bbab1049174ac3cd706260effc4",
    "0x001386a5768cb3d2986dc55608ae9f915f1dcd3b",
    "0x001432765e0868fef159445fa8b6be2ae1cffac3",
    "0x0014501755a9fb7a6350793a7e3744764e65f695",
    "0x0014971dba5b1481296e6abdd7234b0d8474bb8c",
    "0x0014e0ae2d3d4ddb3cb31581649e41a04e36b2fb",
    "0x00152cdf95e0e8da213aa6ad84f10fe459e4fd86",
    "0x00156fb2f2fbb0fed39f890a4326c038d382e864",
    "0x00159b196b10fce2b205eafb178bfd09b69017ab",
    "0x0015c83f21f8733683b94723d8aac29eddd68581",
    "0x0015d941c6f83e0b664447573e8bbab9138efa18",
    "0x001640f5a3867ec5eb4efecc350a4c65e2237be5",
    "0x0016467363b9516d4537f71d0809e12b41cc78c5",
    "0x00164b05e30144bdfa48c5bf1d42ce6e6c83b3a8",
    "0x00166214f0dc62ad02bdd129ca4011ec6b2f0ccf",
    "0x00167e2cd576f63d91700a2d4c2e60b01872a306",
]


def fetch_single_wallet(wallet_address, size=100):
    url = "https://api.syve.ai/v1/transfers/erc20"
    headers = {"Content-Type": "application/json"}
    _filter = {
        "type": "or",
        "params": {
            "filters": [
                {"type": "eq", "params": {"field": "from_address", "value": wallet_address}},
                {"type": "eq", "params": {"field": "to_address", "value": wallet_address}},
            ]
        },
    }
    body = {
        "filter": {"type": "or", "params": {"filters": [_filter]}},
        "options": [{"type": "size", "params": {"value": size}}],
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    print(response.text)
    data = response.json()
    return data


def fetch_multiple_wallets(wallet_addresses, size=100):
    url = "https://api.syve.ai/v1/transfers/erc20"
    headers = {"Content-Type": "application/json"}
    filters = []
    for wallet_address in wallet_addresses:
        _filter = {
            "type": "or",
            "params": {
                "filters": [
                    {"type": "eq", "params": {"field": "from_address", "value": wallet_address}},
                    {"type": "eq", "params": {"field": "to_address", "value": wallet_address}},
                ]
            },
        }
        filters.append(_filter)
    body = {
        "filter": {"type": "or", "params": {"filters": filters}},
        "options": [{"type": "size", "params": {"value": size}}],
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    data = response.json()
    return data


def test_single_wallet_fetch():
    wallet_address = "0x209c4784ab1e8183cf58ca33cb740efbf3fc18ef"
    data = fetch_single_wallet(wallet_address)
    print(json.dumps(data, indent=4))


def test_multi_wallet_fetch():
    # NOTE: Maximum number of records you can fetch in a single API call is size = 100000
    # - If you need to return more than 100K results you need to paginate using the "cursor"
    data = fetch_multiple_wallets(wallet_addresses, size=10)
    print(json.dumps(data, indent=4))


def main():
    # TODO: Give example with using cursor to paginate results
    test_multi_wallet_fetch()


if __name__ == "__main__":
    main()
