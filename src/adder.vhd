-------------------------------------------------------
--! @file  adder.vhd
--! @brief adder
--! @defgroup adder
-------------------------------------------------------

--! Standard library.
library ieee;
--! Logic elements.
use ieee.std_logic_1164.all;
--! arithmetic functions.
use ieee.numeric_std.all;
--! @brief   adder function
--! @details implementation of adder with cocotb
--! @ingroup adder

entity adder is
  generic (
    g_B10_DATA_WIDTH : integer := 31
    );
  port (
    --# {{comunes|common signals}}
    clk      : in  std_logic;           -- clk
    reset    : in  std_logic;           --rst
    --# {{usuario|User signals}}
    dv       : in  std_logic;           --data_valid_in
    data0_in : in  std_logic_vector(g_B10_DATA_WIDTH-1 downto 0);  -- data_0 input
    data1_in : in  std_logic_vector(g_B10_DATA_WIDTH-1 downto 0);  -- data_1 input
    data_out : out std_logic_vector(g_B10_DATA_WIDTH -1 downto 0);  -- data_out
    dv_out   : out std_logic            -- data_valid_out
    );
end adder;

architecture rtl of adder is

  signal r_sum_out : unsigned(g_B10_DATA_WIDTH-1 downto 0) := (others => '0');
  signal r_dv_out  : std_logic                             := '0';

begin

  -- adder process
  process(clk)
  begin
    if reset = '1' then
      r_sum_out <= (others => '0');
      r_dv_out  <= '0';
    else
      if rising_edge(clk) then
        r_dv_out <= '0';
        if(dv = '1') then
          r_sum_out <= unsigned(data0_in) + unsigned(data1_in);
          r_dv_out  <= '1';
        end if;
      end if;
    end if;
  end process;

  --Outputs
  data_out <= std_logic_vector(r_sum_out);
  dv_out   <= r_dv_out;
end rtl;
