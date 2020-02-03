'use strict'

const fs = require('fs')
const { xor, hexToAscii } = require('./utils')
const findKey = require('./algo')

const c = fs.readFileSync('ciphertexts.txt', 'utf8').split('\n')

const cToFind = c[c.length - 1]

const key = findKey(c, cToFind)
console.log({ key })

console.log(`
==================
Decrypted messages
==================`)
c.map((x, i) =>
    console.log(`(${i+1}) ${hexToAscii(xor(Buffer.from(key, 'hex'), Buffer.from(x, 'hex')).toString('hex'))}`))

// Manually fix errors in some bytes of the key
// ccc = '32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'
// key = '66396e89c9dbd8cc9874352acd6395102eafce78aa7fed28a07f6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a61'
//       'T h e   s e c r e t   m e s s a g e   i s :   W h e n   u s i n g   a   s t r e a m   c i p h e r ,   n e v...........
