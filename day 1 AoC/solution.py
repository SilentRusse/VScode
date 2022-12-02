Main()
        {
            int Wert1 = 0;
            Ergebnisse[];
            Daten[] = File.ReadAllText("data.txt",ReadAllText)
            foreach (var Calorien in Daten)
            {
              Wert1 += Calorien;
                if(Calorien == 0 || Calorien == NULL)
                {
                 int i=0;
                 Ergebnisse[i] = Wert1;
                 i++;
                 Wert1 = 0;
                }
            }
            Console.WriteLine("%1",Ergebnisse.Max());
            Console.ReadLine();
            return 0;