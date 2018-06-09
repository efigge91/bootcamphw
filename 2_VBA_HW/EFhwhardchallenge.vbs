Sub stock_volume_hard_challenge()

    ' Set an initial variable for worksheets
    Dim iIndex As Integer
    Dim ws As Excel.Worksheet

        ' Cycle through worksheets
        For iIndex = 1 To ActiveWorkbook.Worksheets.Count
            Set ws = Worksheets(iIndex)
            ws.Activate


             ' Title columns where new data will be stored
            Range("I1") = "Ticker"
            Range("J1") = "Yearly Change"
            Range("K1") = "Percentage Change"
            Range("L1") = "Total Stock Volume"

            ' Set an initial variable for holding the ticker letters
            Dim ticker As String

            ' Set an initial variable for holding the total stock volume per ticker letter
            Dim Total_Stock_Volume As Double
            Total_Stock_Volume = 0
    
            ' Set an initial variable for holding the yearly change
            Dim yearly_change As Double
    
            ' Set an initial variable for values to be used in yearly change
            Dim First_Value As Double
            First_Value = Cells(2, 3)
    
            Dim Final_Value As Double
    
            ' Set an initial variable for holding the percentage change
            Dim percentage_change As Double

            ' Keep track of the location for each ticker letter in the summary table
            Dim ticker_table_row As Integer
            ticker_table_row = 2

            ' Find last row of sheet
            Dim lRow As Long
            lRow = Cells(Rows.Count, 1).End(xlUp).Row
  
                ' Loop through all stocks
                For i = 2 To lRow

                    ' Check if we are still within the ticker letter, if it is not...
                    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

                        ' Set the ticker letter
                        ticker = Cells(i, 1).Value

                        ' Add to the stock volume for that ticker
                        Total_Stock_Volume = Total_Stock_Volume + Cells(i, 7).Value
    
                        ' Store the final value of the stock
                        Final_Value = Cells(i, 6)
    
                        ' Find the Yearly Change
                        yearly_change = Final_Value - First_Value
    
                            ' Find the percentage change
                            If First_Value = 0 Then
                            percentage_change = yearly_change
                            Else
                            percentage_change = yearly_change / First_Value
                            End If
                        
                        ' Print the summary table
                        Range("I" & ticker_table_row).Value = ticker
                        Range("J" & ticker_table_row).Value = yearly_change
                        Range("K" & ticker_table_row).Value = FormatPercent(percentage_change)
                        Range("L" & ticker_table_row).Value = Total_Stock_Volume

                        ' Add one to the summary table row
                        ticker_table_row = ticker_table_row + 1
      
                        ' Reset the total stock volume
                        Total_Stock_Volume = 0
    
                        ' Reset the Initail Value for the next yearly change
                        First_Value = Cells(i + 1, 3)
    
                    ' If the cell immediately following a row is the same ticker letter...
                    Else

                    ' Add to the total stock volume
                    Total_Stock_Volume = Total_Stock_Volume + Cells(i, 7).Value
    
                End If
    
            Next i

        'Conditionally Format Yearly Change
        For j = 2 To lRow

            If (Cells(j, 10) > 0) Then
            Cells(j, 10).Interior.ColorIndex = 4
        
            End If
    
            If (Cells(j, 10) < 0) Then
            Cells(j, 10).Interior.ColorIndex = 3

            End If

        Next j

    ' Title columns where new data will be stored
    Range("O2") = "Greatest % Increase"
    Range("O3") = "Greatest % Decrease"
    Range("O4") = "Greatest Total Volume"
    Range("P1") = "Ticker"
    Range("Q1") = "Value"
    
    ' Set an initial value for second ticker column
    Dim ticker_table_row_two As Integer
    ticker_table_row_two = 2
    
    Dim ticker_table_row_three As Integer
    ticker_table_row_three = 3
    
    Dim ticker_table_row_four As Integer
    ticker_table_row_four = 4
    
    ' Set an initial value for Greatest % Increase
    Dim MaxPercent As Double
    MaxPercent = Cells(2, 11).Value
    
    ' Set an initial value for Greatest % Decrease
    Dim MinPercent As Double
    MinPercent = Cells(2, 11).Value
    
    ' Set an initial value ofr Greatest Total Volume
    Dim MaxVolume As Double
    
    MaxVolume = Cells(2, 12).Value

    ' Set an initial value for new last row
    Dim lRowTwo As Long
    lRowTwo = Cells(Rows.Count, 9).End(xlUp).Row
    
        ' Loop through new ticker columns
        For i = 2 To lRowTwo

            ' Find maximum in percent column
            If Cells(i, 11).Value > MaxPercent Then
            MaxPercent = Cells(i, 11).Value

            ' Place max percent next to ticker
            ticker = Cells(i, 9).Value
            Range("P" & ticker_table_row_two).Value = ticker
            Range("Q" & ticker_table_row_two).Value = FormatPercent(MaxPercent)
            ticker_table_row_two = ticker_table_row_two

            End If

            ' Find greatest percentage decrease
            If Cells(i, 11).Value < MinPercent Then
            MinPercent = Cells(i, 11).Value

            ' Store ticker next to greatest decrease
            ticker = Cells(i, 9).Value
            Range("P" & ticker_table_row_three).Value = ticker
            Range("Q" & ticker_table_row_three).Value = FormatPercent(MinPercent)
            ticker_table_row_three = ticker_table_row_three

            End If

            ' Find greatest total volume
            If Cells(i, 12).Value > MaxVolume Then
            MaxVolume = Cells(i, 12).Value

            ' Place ticker next to greatest volume
            ticker = Cells(i, 9).Value
            Range("P" & ticker_table_row_four).Value = ticker
            Range("Q" & ticker_table_row_four).Value = MaxVolume
            ticker_table_row_four = ticker_table_row_four

            End If

        Next i

    Next iIndex

End Sub