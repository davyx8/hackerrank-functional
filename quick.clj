(defn quicksort [[ pivot & coll ]]
 (when pivot 
    (concat (quicksort (filter ( fn [x] (< x pivot )) coll)
     [pivot]
            (quicksort (filter ( fn [x] (>= x pivot ) ) coll) )
      ))))
