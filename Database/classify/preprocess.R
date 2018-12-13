txtdata <- read.table("list_attr_img.txt", header = FALSE)
##개오래걸림

class1 <- read.table("class/class1.txt", header = FALSE)
class2 <- read.table("class/class2.txt", header = FALSE)
class3 <- read.table("class/class3.txt", header = FALSE)
class4 <- read.table("class/class4.txt", header = FALSE)
class5 <- read.table("class/class5.txt", header = FALSE)

rand <- sort(sample(1:289222,10000,replace=F))

test<-txtdata[rand,]
class1_test<-txtdata[rand,c(1,class1[,1])]
class2_test<-txtdata[rand,c(1,class1[,1])]
class3_test<-txtdata[rand,c(1,class1[,1])]
class4_test<-txtdata[rand,c(1,class1[,1])]
class5_test<-txtdata[rand,c(1,class1[,1])]

write.table(test, "test.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class1_test, "class1_test.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class2_test, "class2_test.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class3_test, "class3_test.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class4_test, "class4_test.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class5_test, "class5_test.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)

rand_for_all<-sort(sample(rand,1000,replace=F))
test_product<-txtdata[rand_for_all,]
class1_product<-txtdata[rand_for_all,c(1,class1[,1])]
class2_product<-txtdata[rand_for_all,c(1,class1[,1])]
class3_product<-txtdata[rand_for_all,c(1,class1[,1])]
class4_product<-txtdata[rand_for_all,c(1,class1[,1])]
class5_product<-txtdata[rand_for_all,c(1,class1[,1])]

write.table(test_product, "test_product.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class1_product, "class1_product.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class2_product, "class2_product.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class3_product, "class3_product.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class4_product, "class4_product.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
write.table(class5_product, "class5_product.txt",row.names = FALSE, col.names = FALSE,quote = FALSE)
