'use strict'

const { xor, splitHexStr } = require('./utils')

const findKey = (c, ccc) => {
    let key = new Array(ccc.length / 2).fill(null)

    for (let i = 0; i < c.length; i++) {

        let spacesSuspicious = new Array(ccc.length / 2).fill(0)
        let ci = Buffer.from(c[i], 'hex')

        for (let j = 0; j < c.length; j++) {
            if (i === j) continue

            let xorVal = splitHexStr(
                xor(ci, Buffer.from(c[j], 'hex')).toString('hex'))

            for (let k = 0; k < xorVal.length; k++) {
                if (parseInt(xorVal[k], 16) >= 65 &&
                        parseInt(xorVal[k], 16) <= 90) {
                    // Probably a space in one of two xored strings
                    spacesSuspicious[k]++
                }
            }
        }

        for (let j = 0; j < spacesSuspicious.length; j++) {
            if (spacesSuspicious[j] >= 6) {
                // There is a space on pos. j in string c[i]
                // That's why if we xor c[i][j] with space we'll have key[i][j]
                key[j] = splitHexStr(
                    xor(
                        ci,
                        Buffer.from(
                            new Array(ccc.length).fill(20).join(''), 'hex')
                    ).toString('hex')
                )[j]
            }
        }
    }

    key = key.map(x => x ? x : '00')
    key = key.join('')

    return key
}

module.exports = findKey
