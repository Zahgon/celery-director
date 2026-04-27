import base64
import hashlib
from pathlib import Path
from urllib.request import urlretrieve

import click

from director.context import pass_ctx

DEPENDENCIES = [
    (
        "https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.min.js",
        "sha256-ngFW3UnAN0Tnm76mDuu7uUtYEcG3G5H1+zioJw3t+68=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/vue-router@3.3.4/dist/vue-router.min.js",
        "sha256-87g98o5+aw7/ExJ9tBjvH8zz46FJ7hiylPtNFcPvsSw=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/vuex@3.1.2/dist/vuex.min.js",
        "sha256-LfE9mPMjeOg3dTn1sESY2Xvdbq7gAhONtkxacnr7FSA=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/vuetify@2.3.8/dist/vuetify.min.js",
        "sha256-b4RV6u+xflpPubfyN5gdooQRpDjROUcaCCSWbKQNX9Y=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/moment@2.24.0/min/moment.min.js",
        "sha256-4iQZ6BVL4qNKlQ27TExEhBN1HFPvAvAMbFavKKosSWQ=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/axios@0.19.0/dist/axios.min.js",
        "sha256-S1J4GVHHDMiirir9qsXWc8ZWw74PHHafpsHp5PXtjTs=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/d3@5.16.0/dist/d3.min.js",
        "sha256-Xb6SSzhH3wEPC4Vy3W70Lqh9Y3Du/3KxPqI2JHQSpTw=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/dagre-d3@0.6.4/dist/dagre-d3.min.js",
        "sha256-dPm4TA8Y9PY5q5mmtWMkRGOCMHJDKy34ZrxdbBGA9cs=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/vuetify@2.3.8/dist/vuetify.min.css",
        "sha256-aS2abSwj+AMqtAmTglCnsg9GkAyDUKSCFd4xNdLX/AA=",
        None,
    ),
    (
        "https://cdn.jsdelivr.net/npm/@mdi/font@5.5.55/css/materialdesignicons.min.css",
        "sha256-HCkcFMiRi/WMAXrgcUj/C5aoUrPtvHxpfbOIlwdsNtg=",
        "mdi",
    ),
    (
        "https://fonts.gstatic.com/s/roboto/v20/KFOkCnqEu92Fr1MmgVxFIzIXKMnyrYk.woff2",
        "sha256-zlHOyHhuN60+uGhmzvAy+DRFPdAFH1q7iQet5ST8m1E=",
        "fonts",
    ),
    (
        "https://cdn.jsdelivr.net/npm/@mdi/font@5.5.55/fonts/materialdesignicons-webfont.woff2",
        "sha256-6PFQMmcHK85n15RxAODS3QGyyNG04kPtO+pFnw+Ud/c=",
        "fonts",
    ),
]


def compute_sri_hash(filename, block_size=4096):
    """
    Compute a SRI-compliant hash with SHA256
    :param filename: path to the file
    :param block_size: size of the block for reading binary data
    :return: a base64-encoded hash
    """
    pass


@click.command()
@pass_ctx
def dlassets(ctx):
    """Download the required static assets"""
    pass
