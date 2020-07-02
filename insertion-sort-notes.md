	When making comparison at beginning of sort, you have a pair of items: a key (the item to move), and the rest of the set, against which the key will be compared.

	The loop invariant will be this subset precedes the key and the rest of the set will sorted. It will go from being an empty array to an array the size of the original. 

====

	You have three partitions of the set: a sorted partition, a key (single element), and unsorted partition. This key will separate the sorted/unsorted partitions.

	When inserting a given key, this key is taken from the head of the unsorted partition. The sorted partition's tail will then start to shift, which means that prior to the actual insertion, this sorted partition will have one duplicate on each iteration of the insertion loop.
	This shift routine 
