from json import dumps
from base64 import b64encode

def crypt(key, data):
    S = list(range(256))
    j = 0

    for i in list(range(256)):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    j = 0
    y = 0
    out = []

    for char in data:
        j = (j + 1) % 256
        y = (y + S[j]) % 256
        S[j], S[y] = S[y], S[j]

        out.append(chr(ord(char) ^ S[(S[j] + S[y]) % 256]))

    return ''.join(out)

print(b64encode(crypt("¨8/VI{ÇbÍßtÊZðJ3ÒecOÆJâ¶Qÿ7ïs", dumps({
    "fingerprint_version": 43,
    "timestamp": "2025-05-10T16:44:57.184Z",
    "math_rand": "a4493ad9c9c66",
    "webasm": True,
    "document": {
        "title": "Vous connecter à votre compte Epic Games | Epic Games",
        "referrer": ""
    },
    "navigator": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "platform": "Win32",
        "language": "fr-FR",
        "languages": [
            "fr-FR",
            "fr",
            "en-US",
            "en"
        ],
        "hardware_concurrency": 4,
        "device_memory": 8,
        "product": "Gecko",
        "product_sub": "20030107",
        "vendor": "Google Inc.",
        "vendor_sub": "",
        "webdriver": False,
        "max_touch_points": 0,
        "cookie_enabled": True,
        "connection_rtt": 200
    },
    "web_gl": {
        "canvas_fingerprint": {
            "length": 32302,
            "num_colors": 4692,
            "md5": "399cdbb5ee15d69c57357ea31cd2c2ae",
            "tlsh": "72E2F2B122DBFC3EF458C4E822D707984930763DA019076FD8D813AA07674DBDD5A18C"
        },
        "parameters": {
            "renderer": "ANGLE (Intel, Intel(R) UHD Graphics (0x00009B41) Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "vendor": "Google Inc. (Intel)"
        }
    },
    "window": {
        "location": {
            "origin": "https://www.epicgames.com",
            "pathname": "/id/login",
            "href": "https://www.epicgames.com/id/login"
        },
        "history": {
            "length": 2
        },
        "screen": {
            "avail_height": 824,
            "avail_width": 1536,
            "avail_top": 0,
            "height": 864,
            "width": 1536,
            "color_depth": 24
        },
        "performance": {
            "memory": {
                "js_heap_size_limit": 2248146944,
                "total_js_heap_size": 30515188,
                "used_js_heap_size": 27513072
            },
        },
        "device_pixel_ratio": 1.25,
        "dark_mode": False,
        "chrome": True,
    },
    "date": {
        "timezone_offset": -120,
        "format": {
            "calendar": "gregory",
            "day": "2-digit",
            "locale": "fr",
            "month": "2-digit",
            "numbering_system": "latn",
            "time_zone": "Europe/Paris",
            "year": "numeric"
        }
    },
    "runtime": {
        "sd_recurse": False
    },
    "fpjs": {
        "version": "3.4.2",
        "visitor_id": "9b1c405ad3c363cf75fbae02c70ada1a",
        "confidence": 0.6,
        "hashes": {
            "fonts": "a2558384a1d839aeb59a0927e64ab04b",
            "plugins": "7bf9267ddde7a33539244ab8ffe927d5",
            "audio": "81c423152c811da0c92dcbe04435dbfe",
            "canvas": "d2df0cc108804e48707f032c0d5281dd",
            "screen": "6d86cca8bfee34abcddde8290dc1b785"
        }
    },
    "sdk": {
        "caller_stack_trace": "Error\n    at https://talon-website-prod.ecosec.on.epicgames.com/talon_sdk.js:1:399679\n    at Object._0x5205d5 [as execute] (https://talon-website-prod.ecosec.on.epicgames.com/talon_sdk.js:1:399847)\n    at Talon.updateIfNeeded (https://static-assets-prod.unrealengine.com/account-portal/static/assets/index-Bnksxr2S.js:618:66583)\n    at Captcha.updateIfNeeded (https://static-assets-prod.unrealengine.com/account-portal/static/assets/index-Bnksxr2S.js:618:69103)\n    at LoginForm.<anonymous> (https://static-assets-prod.unrealengine.com/account-portal/static/assets/index-Bnksxr2S.js:626:36655)\n    at Generator.next (<anonymous>)\n    at https://static-assets-prod.unrealengine.com/account-portal/static/assets/index-Bnksxr2S.js:2:1060\n    at new Promise (<anonymous>)\n    at br (https://static-assets-prod.unrealengine.com/account-portal/static/assets/index-Bnksxr2S.js:2:849)\n    at https://static-assets-prod.unrealengine.com/account-portal/static/assets/index-Bnksxr2S.js:626:36435"
    },
    "s": 3765414779,
    "solve_token": False
})).encode()).decode())