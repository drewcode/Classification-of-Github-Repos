data = read.csv('pairs.csv')

filtered = data

filtered[, 3] = 1/filtered[, 3]

objects = sort(unique(c(as.character(filtered[, 1]), as.character(filtered[, 2]))))

filtered[, 1] = match(filtered[, 1], objects)
filtered[, 2] = match(filtered[, 2], objects)

n = length(objects)

distanceMatrix = matrix(.Machine$integer.max, n, n)
diag(distanceMatrix) = 0

i <- as.matrix(filtered[-3])
distanceMatrix[i] <- distanceMatrix[i[,2:1]] <- filtered[, 3]

#dist = as.dist(distanceMatrix)
#coor =  cmdscale(dist)
