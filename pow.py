# A very simplified example of proof of work algorithms
#
# @author 
# @assignment CSCI 497 Assignment 3
# @date 8/9/2022


import hashlib
import time

# set to 2 ** 32 for part C & part D
# set to 2 ** 16 for part E
max_nonce = 2 ** 16


def proof_of_work(header, difficulty_bits):
    # calculate the difficulty target
    target = 2 ** (256 - difficulty_bits)
    for nonce in range(max_nonce):
        # define hash_result based on Problem1.a and Problem1.b
        hash_result = hashlib.sha256((header+str(nonce)).encode('utf-8')).hexdigest()

        # check if this is a valid result, below the target
        if int(hash_result, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hash_result)
            return hash_result, nonce
    # changed nonce in these last two lines to max_nonce - nonce was only assigned in the for loop, so would be
    # destroyed at the end of the loop. Would have caused an error if a valid result was not found.
    print("Failed after %d (max_nonce) tries" % max_nonce)
    return max_nonce


if __name__ == '__main__':
    nonce = 0
    hash_result = ''
    # part 1A:
    initial = "50257206CalebMcMillian"
    initial_hash = hashlib.sha256(initial.encode("utf-8")).hexdigest()
    print("Part 1A:", initial_hash, '\n')

    print("Part 1B: ")
    for nonce in range(31):
        print("Nonce:", nonce, "- Hash:", hashlib.sha256((initial+str(nonce)).encode("utf-8")).hexdigest())

    print("\nParts 1C-1E: ")
    # set to range(31) for part C & part D
    # set to range(16) for part E
    for difficulty_bits in range(16):
        difficulty = 2 ** difficulty_bits
        print("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
        print("Starting search...")

        # checkpoint the current time
        start_time = time.time()

        # make a new block which includes the hash from the previous block
        # we fake a block of transactions - just a string
        new_block = initial + hash_result

        # find a valid nonce for the new block
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

        # checkpoint how long it took to find a result
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed Time: %.4f seconds" % elapsed_time)

        if elapsed_time > 0:
            # estimate the hashes per second
            hash_power = float(int(nonce) / elapsed_time)
            print("Hashing Power: %ld hashes per second" % hash_power)

        print("\n====================\n")
