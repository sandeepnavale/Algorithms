import scala.io.Source
if (args.length > 0) {
    for (line <- Source.fromFile(args(0)).getLines())
        println("Chars in line: "+line.length + " -> " + line)
}
else
    Console.err.println("Please enter filename")