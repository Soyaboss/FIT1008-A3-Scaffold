from data_structures.hash_table import LinearProbeTable
from data_structures.heap import MaxHeap
from landsites import Land

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, n_teams: int) -> None:
        """
        initializes the Mode2Navigator class and assemble the adventurers team according to the number of adventurers inputted. 

        Complexity:
        Best-Case and Worst-Case : O(1)
        
        Explanation
        Creation of hash table and reassignment of data are all done in constant operation. Therefore all operations have complexity of O(1)
        """
    
        self.heap = None
        self.names = None
        self.teams = n_teams
        self.values = []
        self.sites = LinearProbeTable()
        
    def add_sites(self, sites: list[Land]) -> None:
        """
        This method stores and adds land sites to the instance variable self.values, which keeps track of existing land sites. 
        If there are already land sites stored in the object, this method will append the new land sites to the existing ones.

        Complexity:
        Best-case and Worst-case : O(n) where n is the length of the sites
        
        Explanation: 
        he worst-case and best-case scenarios are the same for this method because it only uses the append function, which has a time complexity of O(1), 
        and the set item method in the hash table class, which also has a time complexity of O(1). Since these methods are called within a for loop that iterates over the 
        number of available land sites, the total time complexity of the method is O(n), where n is the total number of land sites.
        """
      
        for site in range(len(sites)):
            self.sites[sites[site].get_name()] = sites[site] #Adds land object to hash table
            self.values.append(sites[site])
          
    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        This method simulates a day of the game and returns a list of tuples containing information about the land ransacked by adventurers and the number of adventurers sent. 
        If the leader decides not to send anyone, the tuple will be (None, 0), indicating that the adventuring team did not ransack any island.

        Complexity:

        Best Case : O(n + k) where n is the number of existing landsites and k is the number of adventure teams participating in the game.
        Worst Case : O(n + k*logn) where n is the number of existing landsites and k is the number of adventure teams participating in the game.
        
        Explanation:
        In this context, the worst-case and best-case scenarios depend on the count_score function. The worst-case scenario occurs when the tuple,
        containing the new maximum score and the land name, does not have the lowest maximum score. In this case, the tuple needs to rise up the heap to be placed 
        at the correct position, potentially requiring adjustments to multiple levels of the heap. Conversely, the best-case scenario occurs when the tuple has the 
        lowest maximum score relative to the other maximum scores in the heap, minimizing the number of adjustments needed for proper placement.
        """
        
        self.organize_score(adventurer_size) 
        list = []
        for _ in range(self.teams): 
            island_score = self.heap.get_max() 
            data = self.count_score(island_score, adventurer_size)   
            if data[0] == 0: #if there is no gold stolen, it means the adventuring team did not send any adventurers
                list.append((None, data[1]))
            else:
                list.append((self.sites[island_score[1]], data[1]))
        return list
    
    def count_score(self, max_land: tuple[int,str], ori_adventurer: int) -> tuple [int,int]: 
        """
        This function updates the score of land sites based on the formula O = 2.5 * C + R, where O is the score, C is the remaining adventure numbers, 
        and R is the gold reward gained on that day. It determines whether the adventurer leader sends a group of adventurers to ransack the island. For instance, 
        if the score of the island is less than 2.5 * C, the leader won't send adventurers there. Conversely, if the score exceeds 2.5 * C, the leader will send adventurers, 
        impacting the maximum score of the land for future adventures.
        
        Complexity:
        Best Case Scenario: O(1) 
        Worst Case Scenario: O(logn) where n is the number of existing landsites

        Explanation:
        In the worst-case scenario, when the score added back to the heap is the highest relative to other scores, the tuple must ascend to the top of the heap.
        This is because the initial operation of the add method appends the tuple to the end of the heap. Conversely, in the best-case scenario,
        when the score added back to the heap is the lowest relative to other scores, the tuple can remain at the same position, benefiting from the initial appending of 
        the tuple to the end of the heap.
        
        """
        
        land = self.sites[max_land[1]]
        if max_land[0] <= (ori_adventurer * 2.5): #If the score is the base score, the adventuring team won't need to send in adventurers
            remaining_score = (2.5 * ori_adventurer)
            lost_gold = 0
            used_adventurers = 0
        else:
            if ori_adventurer >= land.get_guardians(): #Logic when the adventurer is more than the guardians
                remaining_score = (2.5 * ori_adventurer)
                lost_gold = land.get_gold()
                used_adventurers = land.get_guardians()
                land.set_gold(0)
                land.set_guardians(0)
            else:
                lost_gold = min((ori_adventurer * land.get_gold()) / land.get_guardians(), land.get_gold())
                land.set_guardians(land.get_guardians() - ori_adventurer)
                land.set_gold(land.get_gold() - lost_gold)
                used_adventurers = ori_adventurer
                remaining_score = (2.5 * (ori_adventurer - land.get_guardians()) + min((ori_adventurer * land.get_gold()) / land.get_guardians(), land.get_gold())) #Calculate the remaining score after visiting the land
        self.heap.add((remaining_score, max_land[1])) #Add the remaining score to heap
        return (lost_gold, used_adventurers)
        
    
    def organize_score(self, adventurer_number:int) -> None:
        """
        This method constructs a max heap to organize the scores of all the land sites. Each tuple placed into the heap contains two elements: the maximum score of the land based on 
        the input adventurer number, and the name of the land. Priority within the heap is determined by the land with the highest score relative to others.


        Complexity:
        Best-case and Worst-case: O(n) where n is the number of existing land sites
        
        Explanation:
        This method calculates the maximum score of each available land, involving operations with a time complexity of O(1) for calculation, comparison, and variable assignment. 
        Additionally, the append function, used to add tuples containing land scores and names to a list, also has a time complexity of O(1). These operations are applied to all 
        available lands, resulting in a time complexity of O(n), where n is the number of existing land sites.
        After processing all lands, the class method heapify is called to organize the tuples into a Max Heap. heapify employs a bottom-up heap construction approach, 
        sorting sub-heaps and building the final heap. With worst and best-case time complexities of O(n), where n is the number of existing land sites, the total time complexity 
        becomes O(n + n). Ignoring constants, this simplifies to O(n), where n represents the number of existing land sites.
        """
        list = []
        for land in self.values:
            diff = adventurer_number - land.get_guardians()
            if diff >= 0: #if adventurer is more than the guardian, the adventurer gets max gold
                gold = (diff * 2.5) + land.get_gold()
            else:
                gold = (2.5 * (0)) + min((adventurer_number * land.get_gold())/land.get_guardians(), land.get_gold())
                if gold < (adventurer_number * 2.5): #If the score calculated is lower than the base score, take the lowest score
                    gold = (adventurer_number * 2.5)
            list.append((gold, land.get_name()))
        self.heap = MaxHeap.heapify(list)