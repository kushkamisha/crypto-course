'use strict'

// xor of two buffers
const xor = (v1, v2) => Buffer.from(v1.map((elem, i) => v2[i] ^ elem))

const hexToAscii = hex => Buffer.from(hex, 'hex').toString('ascii')

const splitHexStr = str => str.match(/.{1,2}/g)

module.exports = {
    xor,
    hexToAscii,
    splitHexStr,
}
