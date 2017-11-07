function CTD_CheckIsomorphSimple(AG1, AG2: TDistinctGraphStd;
           AIsms: TCTBigMat = nil): boolean;
var
  VCount, i: integer;
  IsoMap: TIntArr;
  Used: TVBoolArr;
  Degrees1, Degrees2: TIntArr;
  IsFindIsm: boolean;

  procedure FindIsom(v1: integer);
  var
    i, v2: integer;
    IsCanMap: boolean;
  begin
    if (v1>=VCount) then begin
      // Найдено изоморфное отображение
      IsFindIsm := true;
      if assigned(AIsms) then AIsms.AddRowDyn(IsoMap) else exit;
    end else begin
      // Поиск вершины v2 второго графа, в которую можно отобразить
      //  вершину v1 первого графа
      for v2 := 0 to VCount-1 do begin
        if ((not Used[v2]) and (Degrees1[v1]=Degrees2[v2])
           and (AG1.VertexDistinctIndex(v1)=AG2.VertexDistinctIndex(v2)))
            then begin
          // Проверяем, может ли вершина v1 быть отображена в v2
          IsCanMap := true;
          for i := 0  to v1-1 do begin
            if (AG1.EdgeDistinctIndex(i, v1)<>AG2.EdgeDistinctIndex(IsoMap[i], v2)) or
               (AG1.EdgeDistinctIndex(v1, i)<>AG2.EdgeDistinctIndex(v2, IsoMap[i])) then begin
              IsCanMap := false;
              break;
            end;
          end;
          // Если может - отображаем, и рекурсивно продолжаем для вершины v1+1
          if (IsCanMap) then begin
            Used[v2] := true;
            IsoMap[v1] := v2;
            FindIsom(v1+1);
            if IsFindIsm and (not assigned(AIsms)) then exit;
            Used[v2] := false;
          end;
        end;
      end; //for v2
    end;
  end;

begin
  if AG1.VertexCount<>AG2.VertexCount then begin
    AIsms.Clear;
    result := false;
    exit;
  end;
  VCount := AG1.VertexCount;
  if assigned(AIsms) then AIsms.Columns := VCount;
  SetLength(IsoMap, VCount);
  SetLength(Degrees1, VCount);
  SetLength(Degrees2, VCount);
  SetLength(Used, VCount);
  for i := 0 to Pred(VCount) do begin
    Used[i] := false; //лишнее
    Degrees1[i] := AG1.Degree(i);
    Degrees2[i] := AG2.Degree(i);
  end;
  IsFindIsm := false;
  FindIsom(0);
  result := IsFindIsm;
end;