-- Fill in the DistanceConversions module first, and import it here
-- create a higher-order function for converting an area between two dimensions
-- this will take the function for converting a distance, and an area to convert
-- using the functions defined in the DistanceConversions module
-- Example areaConv inchesToCentimetres 9 = 58.0644

import qualified Distance as Dist

sq :: Dist.Distance -> Dist.Distance
sq x = x*x

areaConv :: (Dist.Distance -> Dist.Distance) -> Dist.Distance -> Dist.Distance
areaConv f area = area * (sq (f 1))

-- define a function for converting square inches into square centimetres
sqInToSqCm :: Dist.Distance -> Dist.Distance
sqInToSqCm = areaConv Dist.inToCm 

-- define a function for converting square chains (22 yards) to square metres
sqChainsToSqM :: Dist.Distance -> Dist.Distance
sqChainsToSqM = areaConv Dist.chToM
